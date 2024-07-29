from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = 0
        count = 0
        
        for num in nums:
            if jump < 0:
                return False
            if num > jump:
                jump = num
                count = count + 1
            
            jump = jump - 1
            
        return True
            




s = Solution()
res = s.canJump([3,2,1,0,4])
print(res)