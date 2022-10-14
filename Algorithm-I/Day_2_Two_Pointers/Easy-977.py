"""
https://leetcode.com/problems/squares-of-a-sorted-array/

Related topics:
Arrays

This Easy problem trumped me multiple times. See explanation:
The crux over here is that the array is already sorted.
We are comparing the first and last elements because after square these have the possibility of being the highest element.
Both the extremes contain the max element (after square ofc), so we are inserting these elements to the last of the new
array to make it sorted.
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i , j = 0, len(nums)-1
        res=[]
        while i<=j:
            if abs(nums[i]) >= abs(nums[j]):
                res.insert(0,nums[i]**2)
                i+=1
            else:
                res.insert(0,nums[j]**2)
                j-=1
        return res


s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))
