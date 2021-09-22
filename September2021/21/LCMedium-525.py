"""
https://leetcode.com/problems/contiguous-array/

Variant of Kadane
"""


class Solution:
    def findMaxLength(self, nums) -> str:
        count, maxCount = 0, 0
        table={0:0}
        for i, num in enumerate(nums, 1): # enumerate(nums, 1), 1 is start value of index. Critical for correctness
            if num == 0:
                count -= 1
            else:
                count += 1
            if count in table:
                maxCount = max(maxCount, i-table[count])
            else:
                table[count]=i
        return maxCount

s = Solution()
print(s.findMaxLength([0, 1]))
