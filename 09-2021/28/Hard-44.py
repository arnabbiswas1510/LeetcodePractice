"""
https://leetcode.com/problems/wildcard-matching/

Explanation: https://www.youtube.com/watch?v=3ZDZ-N0EPV0

Standard one in same category: https://leetcode.com/problems/edit-distance/

And:
https://leetcode.com/problems/interleaving-string/
https://leetcode.com/problems/regular-expression-matching/
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp=[[False]*(len(s)+1) for _ in range(len(p)+1)]
        dp[0][0]=True

        for i in range(1,len(p)+1):
            dp[i][0]=dp[i-1][0] if p[i-1]=="*" else False

        for i in range(len(p)):
            for j in range(len(s)):
                if p[i]==s[j] or p[i]=='?':
                    dp[i+1][j+1]|=dp[i][j]
                if p[i]=='*':
                    dp[i+1][j+1]|=dp[i+1][j] or dp[i][j+1]

        return dp[-1][-1]

s = Solution()
print(s.isMatch("adceb", "ab"))
