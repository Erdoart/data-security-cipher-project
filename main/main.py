
import sys
import os

# Shto folderin cipher në path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'cipher'))

# Importo me emrat e saktë të file-ve
from runningkeycipher import running_key_encrypt, running_key_decrypt
from transpositionCipher import double_transposition_encrypt, double_transposition_decrypt

def main():
    print("Zgjidh algoritmin:")
    print("1-> Running Key Cipher")
    print("2-> Double Transposition Cipher")

    choice = input("Zgjedhja: ")

    if choice == "1":
        print("\nRunning Key Cipher")
        plaintext = input("Shkruaj plaintext: ")
        key = input("Shkruaj key (tekst i gjate): ")

        try:
            encrypted = running_key_encrypt(plaintext, key)
            decrypted = running_key_decrypt(encrypted, key)

            print("Encrypted:", encrypted)
            print("Decrypted:", decrypted)
        except ValueError as e:
            print("Gabim:", e)

    elif choice == "2":
        print("\nDouble Transposition Cipher")
        text = input("Shkruaj tekstin: ")
        key1 = input("Shkruaj key 1: ")
        key2 = input("Shkruaj key 2: ")

        try:
            encrypted = double_transposition_encrypt(text, key1, key2)
            decrypted = double_transposition_decrypt(encrypted, key1, key2)

            print("\nRezultatet:")
            print("Encrypted:", encrypted)
            print("Decrypted:", decrypted)

        except ValueError as e:
            print("Gabim:", e)

    else:
        print("Zgjedhje e pavlefshme!")

if __name__ == "__main__":
    main()