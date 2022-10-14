"""
https://leetcode.com/problems/

Related topics: Binary serach with a twist from standard template

The following code is the most generalized binary search template:

def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left


What's really nice of this template is that, for most of the binary search problems, we only need to modify three parts after copy-pasting this template, and never need to worry about corner cases and bugs in code any more:

Correctly initialize the boundary variables left and right to specify search space. Only one rule: set up the boundary to include all possible elements;
Decide return value. Is it return left or return left - 1? Remember this: after exiting the while loop, left is the minimal k​ satisfying the condition function;
Design the condition function. This is the most difficult and most beautiful part. Needs lots of practice.
"""
from typing import List


class Solution:
    def firstBadVersion(self, n):
        s= 0
        e= len(n)
        while s<e:
            m = s+(e-s)//2
            if n[m] == True:
                e = m
            else:
                s = m+1
        return s

s = Solution()
print(s.firstBadVersion(n=[False, False, False, False, True, True]))
