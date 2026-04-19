import math 

def clean_text(text):
    return ''.join(c for c in text.upper() if c.isalpha())

def get_key_order(key):
    key=clean_text(key)
    if len(key) == 0:
        raise ValueError("Key nuk mund të jetë bosh!")
    return sorted(range(len(key)),key=lambda k:(key[k],k))

def create_matrix(text, cols):
    rows = math.ceil(len(text) / cols)
    matrix = []

    index = 0
    for r in range(rows):
        row = []
        for c in range(cols):
            if index < len(text):
                row.append(text[index])
                index += 1
            else:
                row.append('X')  # padding
        matrix.append(row)

    return matrix


def columnar_encrypt(text, key):
    text = clean_text(text)
    order = get_key_order(key)

    cols = len(key)
    matrix = create_matrix(text, cols)

    ciphertext=""

    for col in order:
        for row in matrix:
            ciphertext += row[col]

    return ciphertext

def columnar_decrypt(ciphertext,key):
    ciphertext = clean_text(ciphertext)
    order = get_key_order(key)

    cols = len(key)
    rows = math.ceil(len(ciphertext) / cols)

    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    index = 0

    for col in order:
        for row in range(rows):
            if index < len(ciphertext):
                matrix[row][col] = ciphertext[index]
                index += 1

    plaintext = ""
    for row in matrix:
        plaintext += ''.join(row)
    
    return plaintext.rstrip('X')


def double_transposition_encrypt(text, key1, key2):
    first=columnar_encrypt(text,key1)
    secound=columnar_encrypt(first,key2)

    return secound

def double_transposition_decrypt(ciphertext, key1, key2):
    first = columnar_decrypt(ciphertext, key2)
    second = columnar_decrypt(first, key1)

    return second




