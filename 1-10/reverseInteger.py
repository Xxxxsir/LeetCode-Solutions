class Solution:
    def reverse(self, x: int) -> int:
        min_value = -2 ** 31
        max_value = 2 ** 31 - 1
        if x < 10 and x > -10:
            return x
        elif x >= 10:
            total = len(str(x))
            cur = ''
            for i in range(total):
                if x%10 == 0:
                    x = x // 10
                    continue
                else:
                    break
            for i in range(len(str(x))):
                cur += (str(x%10))
                x = x // 10
        elif x <= -10:
            x = -x
            total = len(str(x))
            cur = '-'
            for i in range(total):
                if x%10 == 0:
                    x = x // 10
                    continue
                else:
                    break
            for i in range(len(str(x))):
                cur += (str(x%10))
                x = x // 10
        if int(cur) < min_value or int(cur) > max_value:
            return 0
        else:
            return int(cur)