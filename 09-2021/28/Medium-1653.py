"""
https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
"""


class Solution:
    def minimumDeletions(self, s: str) -> int:
        total_a = 0
        for c in s:
            total_a+=c=="a"
        if not total_a:
            return 0

        count_b = 0
        res = 99**99

        for c in s:
            res = min(res, total_a+count_b)
            total_a-=c=="a"
            count_b+=c=="b"
        res = min(res, total_a+count_b)
        return res


s = Solution()
print(s.minimumDeletions("aababbab"))
