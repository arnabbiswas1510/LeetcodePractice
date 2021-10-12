"""
https://leetcode.com/problems/delete-and-earn/

See related problem: https://leetcode.com/problems/house-robber/
"""
from typing import List


class Solution:
    def rob(self, nums):
        prev = curr = 0
        for value in nums:
            prev, curr = curr, max(prev + value, curr)
        return curr

    def deleteAndEarn(self, nums):
        points = [0] * 10001
        for num in nums:
            points[num] += num
        return self.rob(points)


s = Solution()
print(s.deleteAndEarn([3,4,2]))
