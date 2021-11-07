"""
https://leetcode.com/problems/masking-personal-information/

Backlog
"""
from typing import List


class Solution:
    def maskPII(self, S):
        at = S.find('@')
        if at >= 0:
            return (S[0] + "*" * 5 + S[at - 1:]).lower()
        S = "".join(i for i in S if i.isdigit())
        return ["", "+*-", "+**-", "+***-"][len(S) - 10] + "***-***-" + S[-4:]


s = Solution()
print(s.maskPII("LeetCode@LeetCode.com"))
