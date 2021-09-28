"""Given an integer number, print it in English."""
""" We can go beyond trillion to decillion by implementimng the following logic """

""" We can also have python library to directly convert given integer to English alphabet 
# pip install inflect 
import inflect
c = inflect.engine()
print(c.number_to_words(123456789123456789123456789123456789))
"""


class NumberToEnglishWord():
    def __init__(self):
        self.d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                  6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
                  11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
                  15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
                  19: 'nineteen', 20: 'twenty',
                  30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
                  70: 'seventy', 80: 'eighty', 90: 'ninety'}
        self.thousand = 1000
        self.million = self.thousand * 1000
        self.billion = self.million * 1000
        self.trillion = self.billion * 1000

    def number_to_words(self, num):
        # restricting the size of number as per below logic conversion up to Trillions
        if len(str(num)) > 15:
            return 'num is too large: %s' % str(num)

        if (num < 20):
            return self.d[num]

        if (num < 100):
            return self.d[num] if (num % 10 == 0) else (self.d[num // 10 * 10] + '-' + self.d[num % 10])

        if (num < self.thousand):
            return self.d[num // 100] + ' hundred' if (num % 100 == 0) else (self.d[num // 100] + ' hundred and ' + self.number_to_words(num % 100))

        if (num < self.million):
            if num % self.thousand == 0:
                return self.number_to_words(num // self.thousand) + ' thousand'
            else:
                return self.number_to_words(num // self.thousand) + ' thousand, ' + self.number_to_words(num % self.thousand)

        if (num < self.billion):
            if (num % self.million) == 0:
                return self.number_to_words(num // self.million) + ' million'
            else:
                return self.number_to_words(num // self.million) + ' million, ' + self.number_to_words(num % self.million)

        if (num < self.trillion):
            if (num % self.billion) == 0:
                return self.number_to_words(num // self.billion) + ' billion'
            else:
                return self.number_to_words(num // self.billion) + ' billion, ' + self.number_to_words(num % self.billion)

        if (num % self.trillion == 0):
            return self.number_to_words(num // self.trillion) + ' trillion'
        else:
            return self.number_to_words(num // self.trillion) + ' trillion, ' + self.number_to_words(num % self.trillion)


c = NumberToEnglishWord()
print(c.number_to_words(123456789123456))
