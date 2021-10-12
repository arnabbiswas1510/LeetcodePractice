"""
https://leetcode.com/problems/pancake-sorting/
"""
from typing import List

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        res = []
        for x in range(len(A), 1, -1):
            i = A.index(x)
            res.extend([i + 1, x])
            A = A[:i:-1] + A[:i]
        return res


s = Solution()
print(s.pancakeSort([3,2,4,1]))
