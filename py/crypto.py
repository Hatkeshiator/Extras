# Cryptography practice
# Problem 0 (feet wet/recap): Implement a basic Caesar (Ave! o/o/o/) cipher.

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
            ciphertext += Alpha[(Alpha.find(char) + 2*shift) % 52]

        else:
            ciphertext += char

    return ciphertext

# Problem 1: Implement an arbitrary substitution cipher.

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

        if char in Alpha:
            ciphertext += key[(Alpha).find(char)]

        else:
            ciphertext += char

    return ciphertext

# Problem 2: Implement a Kasiski* cipher.
# *The Vigenère cipher was not in fact devised by Blaise Vigenère, making it a misnomer. Chiefly to show contempt for convention, I will instead call it the Kasiski cipher, after the man who first devised a systematic attack upon it and defeated the long-standing myth of its impregnability.

kasiski_table = ["   "+alpha+"\n"]
kasiski_table.extend([alpha[i]+"  "+cae(alpha,i) for i in range(26)])

def kas(plaintext: str, key: str = "key") -> str:

    ciphertext = ""
    keyi = 0
    for i in range(len(plaintext)):

        ## print("iteration", i)

        char = plaintext[i]
        keychar = key[keyi % len(key)]
        shift = Alpha.find(keychar.lower()) // 2

        if char in Alpha:
            ciphertext += Alpha[(Alpha.find(char) + 2 * shift) % 52]
            ## print(char, "+", keychar, "(", shift, ") =", ciphertext[-1])
            keyi += 1
        else:
            ciphertext += char

    return ciphertext

# For the convenience of those who use the misnomer.
def vig(a, b):
    return kas(a, b)
