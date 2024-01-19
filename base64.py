sf_digits = [x for x in range(64)]
sf_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/"

# the div function on a pair of numbers returns the first divided by the number which is formed when sixty-four is raised to the power of the other.

def b64_div(a, i):
    result = int(a // (64 ** i))
    return result

# the check function tells you how many characters are in the base 64 string equivalent to the input decimal integer

def b64_check(a):
    i = 0
    while b64_div(a,i) != 0:
        i += 1
    if i == 0:
        i = 1
    return i

# the core function on a number returns the leftmost digit in its base 10 representation.

def b64_core(a):
    i = b64_check(a) - 1
    #print(i)
    # b64_div(a, i) == leftmost character of b64_string(a)

    digit = b64_div(a, i)
    #print(digit)
    return digit

# the digits function loops over and over telling you what each digit should be. Returns an array of type int, decribing the digits from leftmost to rightmost

def b64_digits(a):
    i = b64_check(a)
    digits = []
    for x in range(i):
        # i - x should be equal to b64_check(a)
        if b64_check(a) != (i - x):
            digits.append(0)
            continue
        digit = b64_core(a)
        digits.append(digit)
        a -= digit * 64 ** ((i - 1) - x)
        #print(a, digits)
    return digits

# the string function returns a string representing the base 64 equivalent (output) of a base 10 integer (input)

def b64_string(a):
    digits = b64_digits(a)
    string = ""
    for item in digits:
        string += sf_chars[item]
    return string

# the core decode function returns the int value that the char in the base 64 string

def b64_decode_core(char):
    i = 0
    for x in range(len(sf_chars)):
        if char == sf_chars[x]:
            i = x
    return i

# the digits decode function returns the array that would be formed if the original base 10 number were used as input to b64_digits

def b64_decode_to_digits(string):
    digits = []
    for char in string:
        digits.append(b64_decode_core(char))
    return digits

# the decode function decodes a base 64 string to a base 10 one

def b64_decode(string):
    digits = b64_decode_to_digits(string)
    result = 0
    for x in range(len(digits)):
        result += (digits[len(digits)-(x+1)] * 64 ** x)
    return result

def b64_dbg(a):
    return a == b64_decode(b64_string(a))

def b64_printstuff(a):
    print(a,b64_string(a),b64_decode(b64_string(a)),b64_debug(a))

# TODO: b64_string(2664879) is misbehaving
