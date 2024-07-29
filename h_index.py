from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:

        k = len(citations)
        
        for i in range(0, k):
            if k - i <= citations[i]:
                return k - i
        
        return 0
        
s = Solution()
n = s.hIndex([3,0,6,1,5])
print(n)