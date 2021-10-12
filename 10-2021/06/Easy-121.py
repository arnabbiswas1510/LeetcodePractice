"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Modification of kadane. This Algo becomes Kadane if the diff of the prices are given (coz the diff can be -ve)
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit

    def maxProfitKadane(self, prices: List[int]) -> int:
        maxCurr, maxSoFar = 0, 0
        for i in range(len(prices)):
            maxCurr = max(0, maxCurr + (prices[i] - prices[i-1]))
            maxSoFar = max(maxCurr, maxSoFar)
        return maxSoFar

s = Solution()
print(s.maxProfit([1, 7, 4, 11]))
print(s.maxProfitKadane([0, 6, -3, 7])) #For price deltas
