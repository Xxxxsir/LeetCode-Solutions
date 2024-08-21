class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        length = len(s)
        sub_str = s[0]
        for i in range(1,len(s)+1):
            for j in range(len(s)+1-i):
                if s[j:j+i+1] == s[j+i-length:j-length-1:-1]:
                    if len(s[j:j+i+1]) > longest:
                        longest = len(s[j:j+i+1])
                        sub_str = s[j:j+i+1]
        
        return sub_str