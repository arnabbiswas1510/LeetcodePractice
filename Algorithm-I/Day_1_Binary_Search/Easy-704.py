"""
https://leetcode.com/problems/binary-search/

Related topics:
"""
from typing import List

class Solution:
    def binarySearch(self, nums, lo, hi, target):
        mid=lo+(hi-lo)//2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            return self.binarySearch(nums, lo, mid-1, target)
        else:
            return self.binarySearch(nums, mid+1, hi, target)


    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi -lo)//2
            if target <= nums[mid]:
                hi = mid
            else:
                lo = mid+1
        return lo if nums[lo] == target else -1


s=Solution()
print(s.search( nums = [-1,0,3,5,9,12], target = 12))