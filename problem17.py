#! /usr/bin/env python

"""

If the numbers 1 to 5 are written out in words:
    one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand)
inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""

from math import floor

NUMBER_TO_WORD_MAP = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "fourty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand"
}


class NumberToWord:
    def __init__(self, number):
        self.number = number

    @staticmethod
    def _single_digit(number):
        return NUMBER_TO_WORD_MAP[number]

    @staticmethod
    def _two_digits(number):
        if number < 20:
            return NUMBER_TO_WORD_MAP[number]

        if number % 10 == 0:
            return NUMBER_TO_WORD_MAP[number]

        decade, single = [int(x) for x in str(number)]
        decade *= 10

        return "{} {}".format(NUMBER_TO_WORD_MAP[decade], NUMBER_TO_WORD_MAP[single])

    def _three_digits(self, number):
        if number % 100 == 0:
            determinator = int(number/100)
            return "{} {}".format(NUMBER_TO_WORD_MAP[determinator], NUMBER_TO_WORD_MAP[100])

        hundred_part = floor(number/100)
        the_rest = int(str(number)[1:])

        return "{} hundred and {}".format(
            NUMBER_TO_WORD_MAP[hundred_part],
            self._two_digits(the_rest)
        )

    def get_word(self):
        if self.number < 10:
            return self._single_digit(self.number)

        if self.number < 100:
            return self._two_digits(self.number)

        if self.number < 1000:
            return self._three_digits(self.number)

        if self.number == 1000:
            return "one " + NUMBER_TO_WORD_MAP[1000]  # Ok I'm lazy


sum_str = ""
for a in range(1, 6):
    h = NumberToWord(a)
    t = h.get_word()
    t = ''.join(t.split())
    print(t)
    sum_str += t
print(len(sum_str))
