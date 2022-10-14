"""
https://leetcode.com/problems/running-sum-of-1d-array/?envType=study-plan&id=level-1

Explanation:

"""
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out = [None] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                out[i] = nums[i]
            else:
                out[i] = out[i-1] + nums[i]
        return out

s = Solution()
print(s.runningSum([1,2,3,4]))
