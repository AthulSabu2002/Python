from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n 
        cpy = nums[:]
        
        for i in range(n):
            index = (i + k) % n
            nums[index] = cpy[i]
        
        return nums
            
            
                
                
            
s = Solution()
nums = [1, 2]
nums = s.rotate(nums, 3)
print(nums)