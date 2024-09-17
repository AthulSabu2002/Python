from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i = 0
        
        while i < n and target >= nums[i]:
            if target == nums[i]:
                return i
            i = i + 1
        
        
        return i
        
        
        
s = Solution()
index = s.searchInsert([1,3,5,6], 7)        
print(index)