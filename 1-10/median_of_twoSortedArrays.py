class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        length = len(nums1)+len(nums2)
        target = length//2+1
        
        merged = []
        i,j = 0,0
        while i<len(nums1) and j<len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

            if len(merged) == target:
                break
        
        while i<len(nums1):
            merged.append(nums1[i])
            i += 1
            if len(merged) == target:
                break

        while j<len(nums2):
            merged.append(nums2[j])
            j += 1
            if len(merged) == target:
                break
        
        if length%2 == 1:
            return merged[target-1]
        else :
            return (merged[target-1]+merged[target-2])/2
