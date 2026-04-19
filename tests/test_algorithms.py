import sys
import os

#folderi prind dhe folderin cipher në path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cipher_dir = os.path.join(parent_dir, 'cipher')

sys.path.insert(0, parent_dir)
sys.path.insert(0, cipher_dir)

# Importo modulet
from runningkeycipher import running_key_encrypt, running_key_decrypt
from transpositionCipher import double_transposition_encrypt, double_transposition_decrypt

def test_running_key():
    """Teston Running Key Cipher"""
    print("\nTESTING RUNNING KEY CIPHER...")
    
    plaintext = "HELLO"
    key = "THISISALONGKEY"
    
    encrypted = running_key_encrypt(plaintext, key)
    decrypted = running_key_decrypt(encrypted, key)
    
    assert decrypted == plaintext.upper().replace(" ", ""), f"Gabim: {decrypted} != {plaintext}"
    print(f"Running Key Cipher: '{plaintext}' -> '{encrypted}' -> '{decrypted}'")
    return True

def test_double_transposition():
    """Teston Double Transposition Cipher"""
    print("\nTESTING DOUBLE TRANSPOSITION CIPHER...")
    
    plaintext = "HELLOWORLD"
    key1 = "CIPHER"
    key2 = "KEY"
    
    encrypted = double_transposition_encrypt(plaintext, key1, key2)
    decrypted = double_transposition_decrypt(encrypted, key1, key2)
    
    assert decrypted == plaintext.upper().replace(" ", ""), f"Gabim: {decrypted} != {plaintext}"
    print(f"Double Transposition: '{plaintext}' -> '{encrypted}' -> '{decrypted}'")
    return True

def test_edge_cases():
    """Teston raste speciale"""
    print("\nTESTING EDGE CASES...")
    
    # Test me tekst të gjatë
    plaintext = "THIS IS A VERY LONG SECRET MESSAGE THAT NEEDS TO BE ENCRYPTED"
    key = "a" * 50
    key1 = "SECRET"
    key2 = "KEY"
    
    # Running Key test
    encrypted_rk = running_key_encrypt(plaintext, key)
    decrypted_rk = running_key_decrypt(encrypted_rk, key)
    assert decrypted_rk == plaintext.upper().replace(" ", "")
    print("Running Key me tekst të gjatë")
    
    # Double Transposition test
    encrypted_dt = double_transposition_encrypt(plaintext, key1, key2)
    decrypted_dt = double_transposition_decrypt(encrypted_dt, key1, key2)
    assert decrypted_dt == plaintext.upper().replace(" ", "")
    print("Double Transposition me tekst të gjatë")
    
    return True

def run_all_tests():
    """Ekzekuton të gjitha testet"""
    print("\n" + "="*50)
    print("TESTIMI I ALGORITMEVE TË ENKRIPTIMIT")
    print("="*50)
    
    tests_passed = 0
    tests_failed = 0
    
    try:
        if test_running_key():
            tests_passed += 1
        else:
            tests_failed += 1
    except Exception as e:
        print(f"Running Key Cipher dështoi: {e}")
        tests_failed += 1
    
    try:
        if test_double_transposition():
            tests_passed += 1
        else:
            tests_failed += 1
    except Exception as e:
        print(f"Double Transposition dështoi: {e}")
        tests_failed += 1
    
    try:
        if test_edge_cases():
            tests_passed += 1
        else:
            tests_failed += 1
    except Exception as e:
        print(f"Edge cases dështuan: {e}")
        tests_failed += 1
    
    print("\n" + "="*50)
    print(f"REZULTATI: {tests_passed} teste të suksesshme, {tests_failed} të dështuara")
    print("="*50)
    
    return tests_failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
