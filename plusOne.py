from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if digits[-1] < 9:
            digits[-1] = digits[-1] + 1
            return digits
        else:
            for i in range(n, 0, -1):
                digits = [1] + digits
                return digits
        
s = Solution()
lst = s.plusOne([9, 9, 9])
print(lst)