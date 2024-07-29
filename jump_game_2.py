from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> int:
        maximum = 0
        next_hop = 0
        count = 0
        k = len(nums)
        
        for i in range(0, k):
            maximum = max(i+nums[i], maximum)
            
            if next_hop == i:
                count = count + 1
                next_hop = maximum
                
            
        return count
            




s = Solution()
res = s.canJump([2,1])
print(res)