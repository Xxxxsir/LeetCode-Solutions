class Solution:
    def romanToInt(self, s: str) -> int:
        list  = [('IV',4),('IX',9),('XL',40),('XC',90),('CD',400),('CM',900),
            ('I',1),('V',5),('X',10),('L',50),('C',100),('D',500),('M',1000)]
        num = 0
        while len(s) > 0:
            for symbol,value in list:
                if s[0:2] == symbol:
                    num += value
                    s = s[2:]
                    break
                elif s[0] == symbol:
                    num += value
                    s = s[1:]
                    break
        return num
    
s = "MCMXCIV"
solution = Solution()
print(solution.romanToInt(s)) 