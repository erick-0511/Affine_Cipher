# AFFINE CIPHER

## Description
Python program that implements affine cipher, a substitution cipher.
To encrypt, a formula is used:

<div align="center">E(x) = (ax + b) mod n</div>

Where:
- "a" is in Z<sub>n</sub>
- "x" is the character to encrypt
- "b" is in Z<sub>n</sub>*

To decrypt, a formula is used:

<div align="center">D(x) = (x-b)a<sup>-1</sup> mod n</div>

Where:
- "a<sup>-1</sup>" is the inverse of "a" 
- "x" is the character to decrypt
- "b" is in Z<sub>n</sub>*

In both caes, "n" is the size of the alphabet.

"a" and "b" are elements of the key K = (a, b)

## Characteristics
The program has 2 usage options:
- Write a number (size of the alphabet, n>=2) and get all valid keys and the inverse of a number "a"
- Encrypt with a random key and decrypt

## Execute
py affinecipher.py