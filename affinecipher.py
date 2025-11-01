import math as mt
import random as rd

def ZnStar(n: int) -> list:
    return [z for z in range(1, n) if mt.gcd(z, n) == 1]

def inverse(a: int, n: int) -> int:
    zn = ZnStar(n)
    for i in zn:
        if((a*i)%n == 1):
            return i
        
def keyGeneration(n: int) -> tuple:
    zn = [z for z in range(0, n)]
    znstar = ZnStar(n)    
    a = znstar[rd.randint(0, len(znstar)-1)]
    b =  zn[rd.randint(0, len(zn)-1)]
    return a, b

def allKeys(zn_star:list, zn: list, a: int) -> None:
    if(a in zn_star):
        with open("keys.txt", "w") as f:
            f.write(f"Valid keys for {n}")
            for i in zn_star:
                for j in zn:
                    f.write(f"\nK = ({i}, {j})")
            f.write(f"\n\n{a}^(-1) = {inverse(a, n)}")
            print(f"\nValid keys and a^(-1) are in 'keys.txt'")
    else:
        print("\nInvalid")
    return

def cipher(key: tuple, text: str, alphabet: list) -> str:
    ciphertext = ""
    for c in text:
        if(c in alphabet):
            ciphertext += alphabet[((key[0]*alphabet.index(c)) + key[1])%len(alphabet)]
        else:
            return "ERROR"
    return ciphertext
        
def decipher(key: tuple, text: str, alphabet: list) -> str:
    plaintext = ""
    for c in text:
        if(c in alphabet):
            index = (alphabet.index(c) - key[1]) * inverse(key[0], len(alphabet))
            if(index >= 0):
                plaintext += alphabet[index%len(alphabet)]
            else:
                plaintext += alphabet[len(alphabet) - ((index*-1)%len(alphabet))]
        else:
            return "ERROR"
    return plaintext

if __name__ == "__main__":
    while True:
        print(f"\n\t\t----- OPTIONS -----\n1) Number\n2) Alphabet\n3) Exit")
        option = int(input("Select an option: "))
        if(option==1):
            n = int(input("\nWrite a number: "))
            if(n>=2):  
                zn = [z for z in range(0, n)]
                zn_star = ZnStar(n)
                print(f"\nZn* = {zn_star}\nZn = {zn}")
                a = int(input("Write 'a' -> Zn*: "))
                allKeys(zn_star, zn, a)
            else:
                print("\nInvalid. n>=2")
        elif(option==2):
            ascii = [chr(i) for i in range(32, 127)]
            option_cd = int(input("\n1) Cipher\n2) Decipher\nSelect an option: "))
            text = input("\nWrite a text: ")
            if(option_cd==1):
                cipher_key = keyGeneration(len(ascii))
                print(f"Key: {cipher_key}\nCiphertext: {cipher(cipher_key, text, ascii)}")
            elif(option_cd==2):
                decipher_key = tuple(map(int, input("Key 'a b': ").split()))
                print(f"Plaintext: {decipher(decipher_key, text, ascii)}")
            else:
                print("\nInvalid")
        elif(option == 3):
            break
        else:
            print("\nInvalid")