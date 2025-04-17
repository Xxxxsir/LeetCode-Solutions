class Solution:
    def intToRoman(self, num: int) -> str:
        dict = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
        }
        roman = ''
        length = len(str(num))
        #3407
        for i in range(length):
            digit = num // (10**(length - i -1))
            if digit == 0:
                continue
            if digit == 4 or digit == 9:
                roman += dict[10**(length - i -1)] + dict[(digit+1)*10**(length - i - 1)]
            if digit == 5 or digit == 6 or digit == 7 or digit == 8:
                roman += dict[5*10**(length - i - 1)] + dict[10**(length - i - 1)]*(digit-5)
            if digit == 1 or digit == 2 or digit == 3:
                roman += dict[10**(length - i - 1)]*digit
            num -= digit * 10**(length - i - 1)
        
        return roman

