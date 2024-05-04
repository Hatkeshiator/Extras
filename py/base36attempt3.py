st_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
st_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# the div function on a pair of numbers returns the first raised to the power of the other.

def b36_div(a, i):
    result = int(a // (36 ** i))
    return result

# the check function tells you how many characters are in the base 36 string equivalent to the input decimal integer

def b36_check(a):
    i = 0
    while b36_div(a,i) != 0:
        i += 1
    if i == 0:
        i = 1
    return i

# the core function on a number returns the leftmost digit in its base 10 representation.

def b36_core(a):
    i = b36_check(a) - 1
    
    # b36_div(a, i) == leftmost digit of b36(a)

    digit = b36_div(a, i)
    return digit

# the digits function loops over and over telling you what each digit should be. Returns an array of type int, decribing the digits from leftmost to rightmost

def b36_digits(a):
    i = b36_check(a)
    digits = []
    for x in range(i):
        digit = b36_core(a)
        digits.append(digit)
        a -= digit * 36 ** ((i - 1) - x)
    return digits

# the string function returns a string representing the base 36 equivalent (output) of a base 10 integer (input)

def b36_string(a):
    digits = b36_digits(a)
    string = ""
    for item in digits:
        string += st_chars[item]
    return string

# the debug function checks [whatever you want] for errant output

def b36_debug():
    dbg_arr = [x for x in range(10000)]
    for x in dbg_arr:
        if int(b36_string(x), base = 36) != x:
            print(f"{x}, {b36_string(x)}; {int(b36_string(x), base = 36)}")
            print(int(b36_string(x), base = 36) == x)
