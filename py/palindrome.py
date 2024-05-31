def ispal(number):
    digits = []
    for char in str(number):
        digits.append(int(char))
    temp = []
    for x in range(len(digits) - 1, -1, -1):
        temp.append(digits[x])
    result = digits == temp
    return result

def main():
    a = input("Enter a number")
    print(ispal(a))