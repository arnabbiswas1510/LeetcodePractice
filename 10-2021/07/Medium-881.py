"""
https://leetcode.com/problems/boats-to-save-people/
"""
from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        i, j = 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] <= limit:
                j -= 1
            i += 1
        return i


s = Solution()
print(s.numRescueBoats([3,2,2,1],3))
