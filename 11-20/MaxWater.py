class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        volume = 0
        for i in range(1, n):
            for j in range(n - i):
                temp = i * min(height[j], height[j + i])
                if temp > volume:
                    volume = temp

        return volume

# Two pointers
class Solution:
    def maxArea(self, height: List[int]) -> int:
        volume = 0
        left = 0
        right = len(height) - 1
        while left < right:
            temp = min(height[left], height[right]) * (right - left)
            if temp > volume:
                volume = temp
            if height[left] > height[right]:
                right = right - 1
            else:
                left += 1

        return volume