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

sub_key = "BbAaDdCcFfEeHhGgJjIiLlKkNnMmPpOoRrQqTtSsVvUuXxWwZzYy"

## import random as rand
## flag, sub_key, used_chars = False, "", []
## while not flag:
##     flag = False
##     k = rand.randint(0,51)
##     c = Alpha[k]
##     if c not in used_chars:
##         sub_key += c
##         used_chars.append(c)
##     if not [char for char in Alpha if char not in sub_key]:
##         flag = True

def set_sub_target(new_target_alphabet: str) -> None:

    if (len(new_target_alphabet) == 52) and (len([c for c in new_target_alphabet if c in Alpha]) == 52):
        global sub_key
        sub_key = new_target_alphabet

    else:
        raise ValueError(f"The target alphabet should be exactly 52 characters long, corresponding to the mapping of the string:\n'{Alpha}'\nand must contain each letter exactly once.")

def sub(plaintext: str, key: str = sub_key) -> str:

    ciphertext = ""

    for char in plaintext:

        if char in Alpha:
            ciphertext += key[(Alpha).find(char)]

        else:
            ciphertext += char

    return ciphertext

# Problem 2: Implement a Kasiski* cipher.
# *The Vigenère cipher was not in fact devised by Blaise Vigenère, making it a misnomer. Chiefly to show contempt for convention, I will instead call it the Kasiski cipher, after the man who first devised a systematic attack upon it and defeated the long-standing myth of its impregnability.

# this is just a printable kasiski table and isn't used anywhere
kas_table = ["   "+alpha+"\n"]
kas_table.extend([alpha[i]+"  "+cae(alpha,i) for i in range(26)])
vig_table = kas_table

def kas(plaintext: str, key: str = "varad") -> str:

    key = key.lower()
    ciphertext = ""
    keyi = 0

    for i in range(len(plaintext)):

        ## print("iteration", i)

        char = plaintext[i]
        keychar = key[keyi % len(key)]
        shift = Alpha.find(keychar) // 2

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

# Decryption
# Probelm 0: Caesar Cipher

def dec_cae(ciphertext: str, known_shift: int) -> str:

     return cae(ciphertext, 26-known_shift) # this shifts to the right instead of to the left, e.g. if shift == 1: ABCD...WXYZ -> ZABC...VWXY; BCDE...XYZA -> ABCD...WXYZ

# Problem 1: Arbitrary substitution cipher.

# given key = sub_key, from above

def dec_sub(ciphertext: str, key: str = sub_key) -> str:

     def generate_counterkey(key: str = key) -> str:
          new_indices = [key.find(char) for char in Alpha] # finds where every letter went
          return "".join([Alpha[i] for i in new_indices]) # finds the counterkey such that sub(key, counterkey) == Alpha.
          # TODO: research the theory on this and try to find out if this can be made simpler

     counterkey = generate_counterkey()
     ## print(sub(key, counterkey) == Alpha
     return sub(ciphertext, counterkey)

# Problem 2: Kasiski cipher

def dec_kas(ciphertext: str, key: str = "varad") -> str:

     key = key.lower()

     def generate_counterkey(key: str = key):
          ## return "".join([Alpha(-Alpha.find(c)) for c in key])
          # efficient but difficult-to-read "simplification" (in the math sense) of the below
          shift_vals = [Alpha.find(c) // 2 for c in key]
          unshift_vals = [-i for i in shift_vals]
          return "".join([Alpha[i * 2] for i in unshift_vals])

     counterkey = generate_counterkey()
     ## print(Alpha == kas(kas(Alpha, key),counterkey)
     return kas(ciphertext, counterkey)

def dec_vig(a, b):
     return dec_kas(a, b)

