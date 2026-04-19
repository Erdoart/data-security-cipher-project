# Data Security Cipher Project

Një projekt edukativ në Python që demonstron dy algoritme klasike të enkriptimit përmes një ndërfaqeje të thjeshtë në command line:

- Running Key Cipher
- Double Transposition Cipher


## Veçoritë

- Enkriptim dhe dekriptim i tekstit nga command line
- Ndarje e qartë mes logjikës së CLI dhe implementimit të algoritmeve
- Normalizim automatik i tekstit në shkronja të mëdha alfabetike
- Teste për të dy algoritmet e implementuara

## Struktura e projektit

- `main.py` - ndërfaqja command-line dhe pika hyrëse e programit
- `ciphers.py` - implementimi i algoritmeve dhe funksioneve ndihmëse
- `test_ciphers.py` - testet e projektit
- `.gitignore` - përjashton fajllat lokalë dhe të gjeneruar

## Kërkesat

- Python 3.10 ose më i ri

## Nisja e projektit

```bash
git clone https://github.com/Erdoart/data-security-cipher-project.git
cd data-security-cipher-project
python main.py --help
```

Në Windows, mund të duhet të përdorësh `py` në vend të `python`, varësisht nga instalimi yt.

## Përdorimi

### Running Key Cipher

Enkriptim:

```bash
python main.py running-key encrypt --text "HELLO" --key-text "XMCKLTHISISALONGKEY"
```

Dekriptim:

```bash
python main.py running-key decrypt --text "EQNVZ" --key-text "XMCKLTHISISALONGKEY"
```

Rezultati i pritur:

- Plaintext: `HELLO`
- Ciphertext: `EQNVZ`

### Double Transposition Cipher

Enkriptim:

```bash
python main.py double-transposition encrypt --text "SECRETMESSAGE" --key1 "KEY" --key2 "DOG"
```

Dekriptim:

```bash
python main.py double-transposition decrypt --text "EARESESSTXEXMCG" --key1 "KEY" --key2 "DOG"
```

Rezultati i pritur:

- Plaintext: `SECRETMESSAGE`
- Ciphertext: `EARESESSTXEXMCG`

## Si funksionon

### Running Key Cipher

Running Key Cipher është një variant i Vigenere Cipher. Në vend që të përdorë një fjalë të shkurtër që përsëritet, ai përdor një tekst më të gjatë si çelës.

Formula e enkriptimit:

`C_i = (P_i + K_i) mod 26`

Formula e dekriptimit:

`P_i = (C_i - K_i) mod 26`

### Double Transposition Cipher

Double Transposition aplikon transpozimin kolonar dy herë:

1. Plaintext-i vendoset në një matricë sipas çelësit të parë.
2. Kolonat lexohen sipas rendit alfabetik të çelësit.
3. Rezultati i ndërmjetëm transpozohet përsëri me çelësin e dytë.

Dekriptimi i kthen këta hapa në rend të kundërt.

## Shënime të rëndësishme

- Përpunohen vetëm shkronjat alfabetike.
- Teksti kthehet në shkronja të mëdha para enkriptimit ose dekriptimit.
- Për Running Key Cipher, teksti i çelësit duhet të ketë të paktën aq shkronja sa teksti hyrës i pastruar.
- Double Transposition përdor `X` si karakter mbushës gjatë enkriptimit.
- Gjatë dekriptimit hiqen `X`-at e tepërta në fund të tekstit.

## Testimi

Për të ekzekutuar testet përdor:

```bash
python -m unittest -v
```


