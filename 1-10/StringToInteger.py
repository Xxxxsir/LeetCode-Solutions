class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = 1
        if not s or s[0] not in '+-0123456789':
            return 0
        elif s[0] in '+-':
            if s[0] == '-':
                sign = -1
            s = s[1:]
        else:
            s = s[0:]
        if not s or s[0] not in '0123456789':
            return 0
        for i in range(len(s)):
            if not s[i].isdigit():
                s = s[:i]
                break
        return max(min(sign * int(s), 2**31 - 1), -2**31)
