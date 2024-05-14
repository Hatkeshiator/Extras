# Cryptography practice
# Problem 1: Implement an arbitrary substitution cipher.

alpha = "abcdefghijklmnopqrstuvwxyz"
ALPHA = alpha.upper()
Alpha = ""
for i in range(26):
     Alpha += ALPHA[i]
     Alpha += alpha[i]

def cae(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    for char in plaintext:
        if char in Alpha:
            pos = Alpha.find(char)
            ciphertext += Alpha[(pos + 2*shift) % 52]
        else:
            ciphertext += char
    return ciphertext

target_Alpha = Alpha

def set_sub_target(new_target_alphabet: str) -> None:
    if len(new_target_alphabet) == 52:
        global target_Alpha
        target_Alpha = new_target_alphabet
    else:
        raise ValueError(f"The target alphabet should be exactly 52 characters long, corresponding to the mapping of the string:\n{Alpha}")

def sub(plaintext: str, key: str = target_Alpha) -> str:
    ciphertext = ""
    for char in plaintext:
        if char in alpha + ALPHA:
            ciphertext += target_Alpha[(Alpha).find(char)]
        else:
            ciphertext += char
    return ciphertext
