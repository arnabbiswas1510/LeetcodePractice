"""
https://leetcode.com/problems/divisor-game/
"""
from typing import List


class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0

s = Solution()
print(s.divisorGame(3))
