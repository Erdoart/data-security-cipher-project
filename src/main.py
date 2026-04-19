from __future__ import annotations

import argparse
import sys

from ciphers import (
    DoubleTranspositionKeys,
    double_transposition_decrypt,
    double_transposition_encrypt,
    running_key_decrypt,
    running_key_encrypt,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Program demonstrues per Running Key Cipher dhe Double Transposition."
    )
    subparsers = parser.add_subparsers(dest="algorithm", required=True)

    rk_parser = subparsers.add_parser("running-key", help="Running Key Cipher")
    rk_parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Menyna e punes")
    rk_parser.add_argument("--text", required=True, help="Teksti hyres")
    rk_parser.add_argument(
        "--key-text",
        required=True,
        help="Tekst i gjate qe sherben si celes (running key)",
    )

    dt_parser = subparsers.add_parser("double-transposition", help="Double Transposition Cipher")
    dt_parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Menyna e punes")
    dt_parser.add_argument("--text", required=True, help="Teksti hyres")
    dt_parser.add_argument("--key1", required=True, help="Celesi i pare i transpozimit")
    dt_parser.add_argument("--key2", required=True, help="Celesi i dyte i transpozimit")
    dt_parser.add_argument(
        "--pad-char",
        default="X",
        help="Karakteri i mbushjes (vetem per encrypt). Default: X",
    )

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.algorithm == "running-key":
        if args.mode == "encrypt":
            result = running_key_encrypt(args.text, args.key_text)
        else:
            result = running_key_decrypt(args.text, args.key_text)
    else:
        keys = DoubleTranspositionKeys(first_key=args.key1, second_key=args.key2)
        if args.mode == "encrypt":
            result = double_transposition_encrypt(args.text, keys, pad_char=args.pad_char)
        else:
            result = double_transposition_decrypt(args.text, keys)

    print(result)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.argv += ["running-key", "encrypt", "--text", "HELLO", "--key-text", "XMCKLTHISISALONGKEY"]
    main()