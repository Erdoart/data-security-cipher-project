# runningkeycipher.py
ALPHABET_SIZE = 26

def _letters_only_upper(text: str) -> str:
    return "".join(ch for ch in text.upper() if ch.isalpha())

def _char_to_num(ch: str) -> int:
    return ord(ch) - ord("A")

def _num_to_char(n: int) -> str:
    return chr((n % ALPHABET_SIZE) + ord("A"))

def running_key_encrypt(plaintext: str, key_text: str) -> str:
    pt = _letters_only_upper(plaintext)
    key = _letters_only_upper(key_text)

    if not pt:
        raise ValueError("Plaintext nuk përmban shkronja.")
    if len(key) < len(pt):
        raise ValueError("Key text duhet të jetë të paktën sa plaintext.")

    key = key[:len(pt)]
    
    ciphertext=""

    for p, k in zip(pt, key):
        p_val = char_to_num(p)
        k_val = char_to_num(k)

        c_val = (p_val + k_val) % 26

        ciphertext += num_to_char(c_val)

    return ciphertext

def running_key_decrypt(ciphertext: str, key_text: str) -> str:
    ct = _letters_only_upper(ciphertext)
    key = _letters_only_upper(key_text)

    if not ct:
        raise ValueError("Ciphertext nuk përmban shkronja.")
    if len(key) < len(ct):
        raise ValueError("Key text duhet të jetë të paktën sa ciphertext.")

    key = key[:len(ct)]
    plaintext = ""

    for c, k in zip(ct, key):
        c_val = char_to_num(c)
        k_val = char_to_num(k)

        p_val = (c_val - k_val) % 26

        plaintext += num_to_char(p_val)
        
    return plaintext
