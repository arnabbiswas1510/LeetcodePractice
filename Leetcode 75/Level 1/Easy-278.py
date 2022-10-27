"""
https://leetcode.com/problems/first-bad-version/

Explanation:
Here you need to return hi or lo

"""
from typing import List


class Solution:
    def firstBadVersion(self, nums):
        lo, hi = 0, len(nums)-1
        while (lo < hi):
            mid = lo + (hi-lo+1)//2
            if nums[mid] == -1:
                hi = mid #Note here u dont do mid-1 since you need to return the value as u r returning hi
            else:
                lo = mid
        return hi

s = Solution()
print(s.firstBadVersion([2,3,5,2,-1-1,-1,-1]))
