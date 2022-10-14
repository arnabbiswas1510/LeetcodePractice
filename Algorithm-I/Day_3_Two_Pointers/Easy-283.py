"""
https://leetcode.com/problems/move-zeroes/

Tricky part was to keep relative ordering the same for all non zero

Related topics:
Arrays
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        nonZeroIndex = 0
        for num in nums:
            if num != 0:
                nums[nonZeroIndex] = num
                nonZeroIndex += 1
        while nonZeroIndex < len(nums):
            nums[nonZeroIndex] = 0
            nonZeroIndex += 1
        return nums


s = Solution()
print(s.moveZeroes(nums=[0,1,0,3,12]))
