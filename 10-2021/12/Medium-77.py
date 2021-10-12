"""
https://leetcode.com/problems/combinations/

Backtracking
"""
from typing import List


class Solution:
    def combine(self, n, k):
        ret = []
        self.dfs(list(range(1, n+1)), k, [], ret)
        return ret

    def dfs(self, nums, k, path, ret):
        if len(path) == k:
            ret.append(path)
            return
        for i in range(len(nums)):
            if len(nums)-i+len(path)>=k:  # This line avoids TLE
                self.dfs(nums[i+1:], k, path+[nums[i]], ret)


s = Solution()
print(s.combine(4,2))
