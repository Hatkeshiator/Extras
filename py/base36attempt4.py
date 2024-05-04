st_digs = [x for x in range(36)]
st_chars = "0123456789abcdefghijklmnopqrstuvwxyz"

def basets_encode(integer):
    number = integer
    digits = []
    negative = False

    if number < 0:
        negative = True
        number = -number
    while number > 0:
        number, digit = divmod(number, 36)
        digits.append(digit)
    digits = digits[::-1]
    string = ''
    if negative:
        string = '-'
    for num in digits:
        string += st_chars[num]
    if integer == 0:
        string = '0'
    return string

def basets_decode(string):
    negative = False
    if string[0] == '-':
        negative = True
        string = string[1:]
    string = string[::-1]
    result = 0
    for x in range(len(string)):
        char = string[x].lower()
        if char in st_chars:
            result += st_chars.index(char) * 36 ** x
        else:
            print("Please only use 0-9 and a-z.")
            result = "TERMINATED: bad value"
            break
    if negative and isinstance(result, int):
        result = -result
    return result
