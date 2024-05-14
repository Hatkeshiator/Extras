# Cryptography practice
# Problem 1: Implement an arbitrary substitution cipher.

def subst(plaintext: str, targetA: str = "DEFGHIJKLMNOPQRSTUVWXYZABC") -> str:
    ciphertext = ""
    for char in plaintext:
        if char in targetA + targetA.lower():
            if char.lower() == char:
                ciphertext += targetA["abcdefghijklmnopqrstuvwxyz".find(char)].lower()
            else:
                ciphertext += targetA["ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(char)]
        else:
            ciphertext += char
    return ciphertext

