from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k = len(prices)
        left = 0
        right = 1
        max_profit = 0
        while right < k:
            currentProfit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit
        
s = Solution()
profit = s.maxProfit([7,6,4,3,1])
print('profit is : ', profit)