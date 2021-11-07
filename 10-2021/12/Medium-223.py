"""
https://leetcode.com/problems/rectangle-area/
"""
from typing import List


class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        overlap = max(min(C,G)-max(A,E), 0)*max(min(D,H)-max(B,F), 0) #See pic to understand this
        return (A-C)*(B-D) + (E-G)*(F-H) - overlap


s = Solution()
print(s.computeArea(-3,0,3,4,0,-1,9,2))

