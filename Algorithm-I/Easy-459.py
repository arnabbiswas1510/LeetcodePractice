"""
https://leetcode.com/problems/

Related topics:
"""
from typing import List


class Solution:
    def XXYYZZ(self, s : str) -> bool:
        length = len(s)
        for i in range(length//2,0,-1):
            numRepeats = length//i
            substring = s[0:i]
            sb=[]
            for j in range(numRepeats):
                sb.append(substring)
            if str(sb) == s:
                return True
        return False


s = Solution()
print(s.XXYYZZ("abcabcabcabc"))
