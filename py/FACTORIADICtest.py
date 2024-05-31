# Factorial Number System implementation. (peter griffin voice: i saw this in a xkcd and thought it was cooler than it was funny)
#
# encode/decode numbers in the [factorial number system](wiki.froth.zone/wiki/Factorial_number_system?lang=en)
# the version is defined as follows:
# simply put: each successive digit is of a base 1 higher than that to its right.
# and formally:
#     the 'first' (rightmost) digit is unary and has the place value of 1 (strictly speaking, 0!)
#     the digit to the left of the first is binary and has the place value of 1 (1!)
#     the next digit to the left is ternary and has the place value of 2 (2!)
#     the next, base 4; with a place value of 6 (3!)
#     keep incrementing both <base> and $\Gamma^{-1}(<placevalue>)$ for each <digit>
#
# so now, we'll make a function that converts an arbitrary number $d_{10}$ in decimal to a number $f_{!}$ in factorial of equivalent value

class Factoriadic_Number:

    def __init__(self, value: list[int]) -> None:

        if not (isinstance(value, list) or isinstance(value, tuple)):
            raise ValueError(f"__init__ method of Factoriadic class expects a homogenous list or tuple of integers as an argument.\n\t(Got {value} instead.)")

        for element in value:
            if not isinstance(element, int):
                raise ValueError(f"__init__ method of Factoriadic class expects a homogenous list or tuple of integers as an argument.\n\t(Found {element}, which is not an integer.)")

        self.value = value


    def __str__(self) -> str:

        result = ''

        for i in self.value:
            result += str(i)
            result += ':'

        result = result[:-1:] # omit trailing :

        return result

def dec2fac(dec_num: int) -> Factoriadic_Number:

    if not (isinstance(dec_num, int) and dec_num >= 0):
        raise ValueError(f"The function dec2fac expects a non-negative integer as the argument.\n\t(Got {dec_num} instead.)")

    result = []
    temp = dec_num

    i = 1
    while temp > 0:
        result.append(temp % i)
        temp //= i
        i += 1

    # handle special case of dec_num == 0
    if dec_num == 0:
        result = [0]

    result.reverse()
    result = Factoriadic_Number(result)

    return result

# and for convenience:
def dec2fac_print(dec_num: int) -> None:
    print(dec2fac(dec_num))

# The inverse logic is dead simple. The way you convert factoriadic numbers to decimal is like any other base conversion.
# Except here, the place values are seen to be the factorial of their index (mathematically, one minux their index. but for us, since python starts at 0, we don't have to worry about that.)
# So in short, $\Sigma^{n}_{i=0} ({f_{{1}}}_{i} \cdot i!)$

from math import factorial


def fac2dec(fac_num: Factoriadic_Number) -> int:

    if not isinstance(fac_num, Factoriadic_Number):
        raise ValueError(f"The function fac2dec expects a factoriadic number as the argument (the raw list or printed string won't work!)\n\t(Got {fac_num} instead.)")

    result = 0

    base = 0
    for i in reversed(fac_num.value):
        result += i * factorial(base)
        base += 1

    return result