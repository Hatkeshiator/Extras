# Take crypto.py and turn it into a module that can be imported, by defining simple classes and methods.

import matplotlib.pyplot as plt

# By default, the alphabet is AaBb...YyZz. However, I aim for the user to be able to define their own alphabet--to e.g. include numbers--so I will not rely on properties of Alpha as defined here.

from string import ascii_uppercase as ALPHA, ascii_lowercase as alpha

Alpha = ""

for i in range(26):
    Alpha += ALPHA[i]
    Alpha += alpha[i]

# Allow debugging and verbose error messages (off by default):

verbose = False

# Single overarching class for plaintext and ciphertext

class text:

    def __init__(self, text: str) -> None:
        self.text = text

    def __str__(self) -> None:
        print(self.text)

    def __repr__(self) -> str:
        return self.text

    def __add__(self, other) -> str:
        return self.text + other.text

    def frequency_dict(self) -> dict:
        freq = {}
        for char in self.text:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        return freq

    def frequency_bar(self) -> None:
        freq = self.frequency_dict()
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        chars, counts = zip(*sorted_freq)
        plt.bar(chars, counts)
        plt.show()

    def set_text(self, new_text: str) -> None:
        self.text = new_text

class plaintext(text):
    def __init__(self, text: str) -> None:
        self.text = text

    def __str__(self) -> None:
        print(self.text)

    def encrypt(self, cipher) -> text:
        return ciphertext(cipher.encrypt(self.text), cipher)

class ciphertext(text):
    def __init__(self, text: str, cipher) -> None:
        self.text = text
        self.cipher = cipher

    def __str__(self) -> None:
        print(self.text)

    def decrypt(self) -> text:
        return plaintext(self.cipher.decrypt(self.text))

    def set_cipher(self, new_cipher) -> None:
        self.cipher = new_cipher

    def ceasar_brute_force(self) -> None:
        for i in range(len(Alpha)):
            shifted = Alpha[i:] + Alpha[:i]
            cipher = substitution(shifted)
            print(f"Shift {i}: {cipher.decrypt(self.text)}")

    def caesar_decrypt(self, shift: int) -> str:
        shifted = Alpha[shift:] + Alpha[:shift]
        cipher = substitution(shifted)
        return cipher.decrypt(self.text)

    def atbash_decrypt(self) -> str:
        atbash = Alpha[::-1]
        cipher = substitution(atbash)
        return cipher.decrypt(self.text)

# Class for all ciphers:

class cipher:
    def __init__(self, key: str) -> None:
        self.cipherkey = key

    def key(self) -> str:
        return self.cipherkey

    def decrypt(self, ciphertext: str) -> str:
        pass

    def encrypt(self, plaintext: str) -> str:
        pass

# Class for Substitution cipher incl. Caesar, Atbash, etc.

class substitution(cipher):
    def check(self) -> None:
        if len(self.cipherkey) != len(Alpha):
            self.cipherkey = Alpha
            if verbose:
                print(f"len(key) != len(Alpha)\n({len(self.alpha)} != {len(Alpha)})")
            raise ValueError("Key must be exactly as long as Alpha. Key reset to Alpha.")
        for char in self.cipherkey:
            if char not in Alpha:
                self.cipherkey = Alpha
                if verbose:
                    print(f"{char} not in Alpha")
                raise ValueError("Every character in the key must be in Alpha. Key reset to Alpha.")
        for char in Alpha:
            if char not in self.cipherkey:
                self.cipherkey = Alpha
                if verbose:
                    print(f"{char} not in key")
                raise ValueError("Every character in Alpha must be in the key. Key reset to Alpha.")

    def __init__(self, key: str) -> None:
        self.cipherkey = key
        self.check()

    def currentkey(self) -> str:
        self.check()
        key = self.cipherkey
        if key == Alpha:
            key = "No key"
        return key

    def decrypt(self, ciphertext: str) -> str:
        self.check()
        plaintext = ""
        for char in ciphertext:
            if char in Alpha:
                plaintext += Alpha[self.cipherkey.find(char)]
            else:
                plaintext += char
        return plaintext

    def encrypt(self, plaintext: str) -> str:
        self.check()
        ciphertext = ""
        for char in plaintext:
            if char in Alpha:
                ciphertext += self.cipherkey[Alpha.find(char)]
            else:
                ciphertext += char
        return ciphertext

    def set_key(self, new_key: str) -> None:
        self.cipherkey = new_key
        self.check()

# Class for Kasiski cipher (see crypto.py)

class kasiski(cipher):
    def __init__(self, key: str) -> None:
        self.cipherkey = key

    def currentkey(self) -> str:
        key = self.cipherkey
        trivial_key = True
        for char in key:
            if char != Alpha[0]:
                trivial_key = False
                break
        if trivial_key:
            key = "No key"
        return key

    def decrypt(self, ciphertext: str) -> str:
        plaintext = ""

        for i in range(len(ciphertext)):
            if ciphertext[i] in Alpha:
                original_char = ciphertext[i]
                original_index = Alpha.find(original_char)
                key_char = self.cipherkey[i % len(self.cipherkey)]
                delta = Alpha.find(key_char)
                new_index = (original_index - delta) % len(Alpha)
                plaintext += Alpha[new_index]
                # can be written in one line:
                #plaintext += Alpha[(Alpha.find(ciphertext[i]) - Alpha.find(self.cipherkey[i % len(self.cipherkey)])) % len(Alpha)]
            else:
                plaintext += ciphertext[i]

        return plaintext

    def encrypt(self, plaintext: str) -> str:
        ciphertext = ""

        for i in range(len(plaintext)):
            if plaintext[i] in Alpha:
                original_char = plaintext[i]
                original_index = Alpha.find(original_char)
                key_char = self.cipherkey[i % len(self.cipherkey)]
                delta = Alpha.find(key_char)
                new_index = (original_index + delta) % len(Alpha)
                ciphertext += Alpha[new_index]
                # can be written in one line:
                #ciphertext += Alpha[(Alpha.find(plaintext[i]) + Alpha.find(self.cipherkey[i % len(self.cipherkey)])) % len(Alpha)]
            else:
                ciphertext += plaintext[i]

        return ciphertext