from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k = len(prices)
        profit = 0
        for i in range(1, k):
            if prices[i] > prices[i - 1]:
                profit = profit + prices[i] - prices[i - 1]
        
        return profit
        
s = Solution()
profit = s.maxProfit([7,1,5,3,6,4])
print('profit is : ', profit)