
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'cipher'))

from runningkeycipher import running_key_encrypt, running_key_decrypt
from transpositionCipher import double_transposition_encrypt, double_transposition_decrypt

def main():
    print("Zgjidh algoritmin:")
    print("1-> Running Key Cipher")
    print("2-> Double Transposition Cipher")

    choice = input("Zgjedhja: ")

    if choice == "1":
        print("\nRunning Key Cipher")

        print("\nZgjedh 1 per Encrypt")
        print("\nZgjedh 2 per Decrypt")
        zgj=input("Zgjedhja: ")
        
        key = input("Shkruaj key (tekst i gjate): ")

        try:
             if zgj=="1":
                plaintext=input("sheno plaintext: ")
                result=running_key_encrypt(plaintext, key)
                print("encrypted: ",result)
                 
             elif zgj=="2":
                ciphertext=input("sheno ciphertext: ")    
                result=running_key_decrypt(ciphertext, key)
                print("Decrypted:", result)
             else:
                 print("zgjedhje e pavlefshme")
        except ValueError as e:
            print("Gabim:", e)

    elif choice == "2":
        print("\nDouble Transposition Cipher")
        
        print("\nZgjedh 1 per Encrypt")
        print("\nZgjedh 2 per Decrypt")
        zgj=input("Zgjedhja: ")
        
        key1 = input("Shkruaj key 1: ")
        key2 = input("Shkruaj key 2: ")

        try:
            if zgj=="1":
                text=input("shkruaj plaintext: ")
                result = double_transposition_encrypt(text, key1, key2)
                print("Encrypted:", result)
            elif zgj=="2":
                text=input("shkruaj ciphertext: ")
                result = double_transposition_decrypt(text, key1, key2)
                print("Decrypted:", result)
            else:
                print("zgjedhje e pavlefshme")
                

        except ValueError as e:
            print("Gabim:", e)

    else:
        print("Zgjedhje e pavlefshme!")

if __name__ == "__main__":
    main()
