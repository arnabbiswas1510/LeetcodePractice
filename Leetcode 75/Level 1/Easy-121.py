"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Explanation:

"""
from typing import List


class Solution:
    def maxProfit(self,prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
