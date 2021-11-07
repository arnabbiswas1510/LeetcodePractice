"""
https://leetcode.com/problems/create-maximum-number/

Greedy, Monotonic Stack
Revisit how the monotonic stack below is being created
"""
from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n, m= len(nums1),len(nums2)
        ret = [0] * k
        for i in range(0, k+1):
            j = k - i #Note: We dont need inner loop here for j
            if i > n or j > m: continue
            left = self.getMax(nums1, i)
            right = self.getMax(nums2, j)
            num = self.mergeMax(left, right)
            ret = max(num, ret)
        return ret

    def mergeMax(self, nums1, nums2):
        ans = []
        while nums1 or nums2:
            if nums1 > nums2:
                ans += nums1[0],
                nums1 = nums1[1:]
            else:
                ans += nums2[0],
                nums2 = nums2[1:]
        return ans

    #Return a monotonic decreasing stack of selects elements
    def maxSingleNumber(self, nums, selects):
        n = len(nums)
        ret = [-1]
        if selects > n : return ret
        while selects > 0:
            start = ret[-1] + 1 #search start
            end = n-selects + 1 #search end
            ret.append( max(range(start, end), key = nums.__getitem__))
            selects -= 1
        ret = [nums[item] for item in ret[1:]]
        return ret

    #This function and maxSingleNumber are interchangable
    def getMax(self, nums, t):
        ans = []
        size = len(nums)
        for x in range(size):
            while ans and len(ans) + size - x > t and ans[-1] < nums[x]:
                ans.pop()
            if len(ans) < t:
                ans += nums[x],
        return ans


s = Solution()
print(s.maxNumber([3,4,6,5], [9,1,2,5,8,3], 5))
