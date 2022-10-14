"""
https://leetcode.com/problems/search-insert-position/

Rules of Binary search:
1. If u use len(nums) then use lo<hi. If u use len(nums)-1 then use lo<=hi

Related topics:
"""
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums)
        while s < e:
            mid = s+(e-s)//2
            if target <= nums[mid]:
                e=mid
            else:
                s=mid+1
        return s


s = Solution()
print(s.searchInsert(nums=[1,3,5,6], target=0))
