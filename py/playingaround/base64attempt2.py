# comments in lowercase are descriptive/document things
# COMMENTS IN UPPERCASE ARE PERSONAL NOTES

# THIS IS CALLED A DICTIONARY I THINK
# NO IT IS NOT, IT IS A LIST
sf_digits = [x for x in range(64)]
sf_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/"

# the to function turns an int into a string that represents its base 64 equivalent.

def basesf_to(integer):
    negative = False
    number = integer
    if number < 0:
        number = 0 - number
        negative = True
    digits = []
    # DIVMOD IS A LIFESAVER
    while number > 0:
        number, digit = divmod(number, 64)
        digits.append(digit)
    # digits is currently backwards, with (the index in sf_chars of) the leftmost digit being the last value
    # LIST SLICING CAN DO THIS
    digits = digits[::-1]
    string = ""
    for num in digits:
        string += sf_chars[num]
    if negative:
        string = "-" + string
    if integer == 0:
        string = "0"
    return string

# the from function takes a base 64 string and decodes it to base 10. If the string is invalid, it terminates with a message.

def basesf_from(string):
    negative = False
    if string[0] == '-':
        string = string[1:]
        negative = True
    string = string[::-1]
    result = 0
    for x in range(len(string)):
        # the if else is just performing a validation while also assigning result. I don't want to iterate over the string twice, especially for some ungodly colossal string
        if string[x] in sf_chars:
            # WHY CAN'T I JUST USE SUBTRACTION HERE?
            result += sf_chars.index(string[x]) * (64 ** x)
        else:
            print("ERROR: NOT A VALID BASE 64 NUMBER")
            result = "TERMINATED"
            break
    # handle negatives
    # if result is not an instance of int, it's because the validation failed and it is now the string "TERMINATED", which makes this part useless
    if negative and isinstance(result, int):
        result = -result
    return result