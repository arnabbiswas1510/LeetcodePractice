"""
https://leetcode.com/problems/move-zeroes/
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: list) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1
        return nums


s = Solution()
print(s.moveZeroes([0,1,0,3,12]))
