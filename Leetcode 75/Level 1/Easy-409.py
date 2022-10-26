"""
https://leetcode.com/problems/longest-palindrome/

Explanation: Neat Solution

"""
from typing import List

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = set()
        for c in s:
            if c not in hash:
                hash.add(c)
            else:
                hash.remove(c)
        # len(hash) is the number of the odd letters
        return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)

s = Solution()
print(s.longestPalindrome("abccccdd"))
