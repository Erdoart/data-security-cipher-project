"""
1) Running Key Cipher
2) Double Transposition Cipher
"""

from __future__ import annotations

import math
from dataclasses import dataclass


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET_SIZE = len(ALPHABET)


def _letters_only_upper(text: str) -> str:
    return "".join(ch for ch in text.upper() if ch.isalpha())


def _char_to_num(ch: str) -> int:
    return ord(ch) - ord("A")


def _num_to_char(value: int) -> str:
    return chr((value % ALPHABET_SIZE) + ord("A"))


def running_key_encrypt(plaintext: str, running_key_text: str) -> str:
    """
    Enkripton plaintext me Running Key Cipher.
    Përdoren vetëm shkronjat A-Z (simbolet e tjera hiqen).
    """

    pt = _letters_only_upper(plaintext)
    key = _letters_only_upper(running_key_text)

    if not pt:
        raise ValueError("Plaintext nuk përmban shkronja për enkriptim.")
    if len(key) < len(pt):
        raise ValueError("Teksti i çelësit duhet të ketë të paktën po aq shkronja sa plaintext.")

    key = key[: len(pt)]
    encrypted = []
    for p_ch, k_ch in zip(pt, key):
        encrypted.append(_num_to_char(_char_to_num(p_ch) + _char_to_num(k_ch)))
    return "".join(encrypted)


def running_key_decrypt(ciphertext: str, running_key_text: str) -> str:
    """
    Dekripton ciphertext me Running Key Cipher.
    Përdoren vetëm shkronjat A-Z (simbolet e tjera hiqen).
    """

    ct = _letters_only_upper(ciphertext)
    key = _letters_only_upper(running_key_text)

    if not ct:
        raise ValueError("Ciphertext nuk përmban shkronja për dekriptim.")
    if len(key) < len(ct):
        raise ValueError("Teksti i çelësit duhet të ketë të paktën po aq shkronja sa ciphertext.")

    key = key[: len(ct)]
    decrypted = []
    for c_ch, k_ch in zip(ct, key):
        decrypted.append(_num_to_char(_char_to_num(c_ch) - _char_to_num(k_ch)))
    return "".join(decrypted)


def _key_order(key: str) -> list[int]:
    """
    Kthen renditjen e kolonave sipas alfabetit të çelësit.
    Për shkronja të njëjta ruan rendin origjinal (stable).
    """

    normalized_key = _letters_only_upper(key)
    if not normalized_key:
        raise ValueError("Çelësi i transpozimit duhet të ketë të paktën një shkronjë.")
    return sorted(range(len(normalized_key)), key=lambda idx: (normalized_key[idx], idx))


def _columnar_transposition_encrypt(text: str, key: str, pad_char: str = "X") -> str:
    cleaned = _letters_only_upper(text)
    if not cleaned:
        raise ValueError("Teksti nuk përmban shkronja për transpozim.")

    order = _key_order(key)
    cols = len(order)
    rows = math.ceil(len(cleaned) / cols)
    padded = cleaned.ljust(rows * cols, pad_char)

    matrix = [padded[r * cols : (r + 1) * cols] for r in range(rows)]

    encrypted = []
    for col_idx in order:
        for row_idx in range(rows):
            encrypted.append(matrix[row_idx][col_idx])
    return "".join(encrypted)


def _columnar_transposition_decrypt(text: str, key: str) -> str:
    cleaned = _letters_only_upper(text)
    if not cleaned:
        raise ValueError("Teksti nuk përmban shkronja për dekriptim transpozimi.")

    order = _key_order(key)
    cols = len(order)
    rows = math.ceil(len(cleaned) / cols)
    total_cells = rows * cols

    # Nëse ciphertext nuk është shumëfish i numrit të kolonave, supozojmë padding.
    padded = cleaned.ljust(total_cells, "X")
    col_length = rows

    columns: dict[int, str] = {}
    cursor = 0
    for col_idx in order:
        columns[col_idx] = padded[cursor : cursor + col_length]
        cursor += col_length

    plain = []
    for row_idx in range(rows):
        for col_idx in range(cols):
            plain.append(columns[col_idx][row_idx])
    return "".join(plain)


@dataclass(frozen=True)
class DoubleTranspositionKeys:
    first_key: str
    second_key: str


def double_transposition_encrypt(
    plaintext: str, keys: DoubleTranspositionKeys, pad_char: str = "X"
) -> str:
    """
    Enkriptim me Double Transposition:
    1) Columnar transposition me first_key
    2) Columnar transposition me second_key
    """

    first_pass = _columnar_transposition_encrypt(plaintext, keys.first_key, pad_char)
    second_pass = _columnar_transposition_encrypt(first_pass, keys.second_key, pad_char)
    return second_pass


def double_transposition_decrypt(ciphertext: str, keys: DoubleTranspositionKeys) -> str:
    """
    Dekriptim me Double Transposition:
    1) Reverse i transpozimit të dytë
    2) Reverse i transpozimit të parë
    """

    first_reverse = _columnar_transposition_decrypt(ciphertext, keys.second_key)
    second_reverse = _columnar_transposition_decrypt(first_reverse, keys.first_key)
    return second_reverse.rstrip("X")
