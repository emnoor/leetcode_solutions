LEVELS = {
    0: "",
    1: "Thousand",
    2: "Million",
    3: "Billion",
}

ONES = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
}

TENS = {
    2: "Twenty",
    3: "Thirty",
    4: "Forty",
    5: "Fifty",
    6: "Sixty",
    7: "Seventy",
    8: "Eighty",
    9: "Ninety",
}

TEENS = {
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
}


def number_to_word_hundreds(num: int) -> str:
    """ Subset of the problem, where num <= 999 """
    s = ""
    if num >= 100:
        s = ONES[num // 100] + " Hundred"
        num %= 100

    if num >= 20:
        s = s + " " + TENS[num // 10]
        num %= 10

    if num >= 10:
        s = s + " " + TEENS[num]
        num = 0

    if num > 0:
        s = s + " " + ONES[num]

    return s.strip()


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        s = ""
        for level in range(4):
            if num > 0:
                part = number_to_word_hundreds(num % 1000)
                if part:
                    s = part + " " + LEVELS[level] + " " + s
                num //= 1000

        return s.strip()
