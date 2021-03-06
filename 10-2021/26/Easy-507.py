"""
https://leetcode.com/problems/perfect-number/
"""
from typing import List


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        ans, SQRT = 0, int(num ** 0.5)
        ans = sum(i + num//i for i in range(1, SQRT+1) if not num % i)
        if num == SQRT ** 2: ans -= SQRT
        return ans - num == num

s=Solution()
print(s.checkPerfectNumber(8128))
