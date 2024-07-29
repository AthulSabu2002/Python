from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = 100000000000000000
        for num in nums:
            if nums.count(num) < count:
                count = nums.count(num)
                single = num
                
        return single
        
s = Solution()
single = s.singleNumber([2, 2, 1])
print(single)