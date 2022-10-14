"""
https://leetcode.com/problems/rotate-array/

Related topics: Arrays

3 Steps:
1. First reverse entire array
2. If u are rotating left reverse the first k elements. If rotating right reverse last k elements
3. Reverse the remaining n-k elements

Alternate approach is to rotateBy1 and then call this method k times. But the cost of this is much higher (nk)
"""
from typing import List

class Solution:
    def reverse(self, nums: List[int], lo: int, hi):
        hi-=1
        mid=lo+(hi-lo)//2
        while lo <= mid:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo +=1
            hi -=1

    def rotate(self, nums: List[int], k: int):
        k %= len(nums) #In case k is larger than len
        self.reverse(nums,0, len(nums))
        self.reverse(nums,0,k)
        self.reverse(nums, k, len(nums))
        return nums

s = Solution()
print(s.rotate(nums=[1,2,3,4,5,6,7], k=3))
