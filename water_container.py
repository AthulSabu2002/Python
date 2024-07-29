from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        k = len(height)  
        i = 0
        vol = 0
        water = 0
        for i in range(0, k):
            for j in range(i+1, k):
                h = min(height[i], height[j])
                area = h * (j - i)
                if vol < area * h:
                     vol = area * h
                     water = area
                     
                    
        return water   
        
s = Solution()
area = s.maxArea([1,2,4,3])
print(area)