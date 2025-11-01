# AFFINE CIPHER

## Description
Python program that implements affine cipher, a substitution cipher.<br>
To encrypt, a formula is used: <br>
<center>E(x) = (ax + b) mod n</center> <br>
where:
- "a" is in Z<sub>n</sub>
- "x" is the character to encrypt
- "b" is in Z<sub>n</sub>*

To decrypt, a formula is used:
<center>D(x) = (x-b)a<sup>-1</sup> mod n</center>
Where:
- "a<sup>-1</sup>" is the inverse of "a" 
- "x" is the character to decrypt
- "b" is in Z<sub>n</sub>*

In both caes, "n" is the size of the alphabet.<br>
"a" and "b" are elements of the key K = (a, b)

## Characteristics
The program has 2 usage options:
- Write a number (size of the alphabet, n>=2) and get all valid keys and the inverse of a number "a"
- Encrypt with a random key and decrypt

## Execute
py affinecipher.py