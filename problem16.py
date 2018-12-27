#! /usr/bin/env python

# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 21000?


def get_digits_of_number(number):
    """ Wouldn't have accepted this function if I stumbled upon
    it in some PR, butt fuck it
    """
    return [int(digit) for digit in str(number)]


if __name__ == "__main__":
    print(sum(get_digits_of_number(2**1000)))
