"""
https://leetcode.com/problems/

Related topics:
"""
from typing import List


class Solution:
    def uglyNumber(self, num: int) -> bool:
        for p in 2, 3, 5:
            while num % p == 0:
                num /= p
        return num == 1

s = Solution()
print(s.uglyNumber(14))
