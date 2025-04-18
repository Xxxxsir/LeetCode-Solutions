class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        for i in range(len(strs[0])):
            for element in strs:
                if i >= len(element):
                    return strs[0][:i]
                if  element[i] != strs[0][i]:
                    return strs[0][:i]
        
        return strs[0]
                