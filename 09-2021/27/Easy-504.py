"""
https://leetcode.com/problems/base-7/
"""

class Solution:
    def convertToBase7(self, num: int) -> str:
        res = ""
        x = 0
        n = abs(num)
        while n > 6:
            x = n % 7
            res = res + str(x)
            n = n//7
        y = (res + str(n))

        if num < 0:
            return "-"+y[::-1]
        else:
            return y[::-1]

s = Solution()
print(s.convertToBase7(100))
