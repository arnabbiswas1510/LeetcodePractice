"""
https://leetcode.com/problems/binary-search

Explanation:

"""

class Solution:
    def search(self, nums, target):
        lo, hi = 0, len(nums)-1
        while (lo < hi):
            mid = lo + (hi-lo+1)//2
            if (target < nums[mid]):
                hi = mid - 1
            else:
                lo = mid
        return lo if nums[lo]==target else -1

s = Solution()
print(s.search([-1,0,3,5,9,12],9))
