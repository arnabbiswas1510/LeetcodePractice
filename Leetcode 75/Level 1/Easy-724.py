"""
https://leetcode.com/problems/

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

    #TODO: Not a smart implementation
    def pivotIndex2(self, nums: List[int]) -> int: #Breaks when i == 0
        rsum = self.runningSum(nums)
        for i in range(len(nums)):
            if i > 0:
                if rsum[i-1] == rsum[len(nums)-1]-rsum[i]:
                    return i
        return -1

    def pivotIndex(self, nums):
        left, right = 0, sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1

s = Solution()
print(s.pivotIndex([2,1,-1]))
