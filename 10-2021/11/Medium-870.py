"""
https://leetcode.com/problems/advantage-shuffle/

Explanation
Sort A
For every element b in B from big to small,
if A[-1] > b,
then this b will take the biggest element in A by A.pop().
otherwise take the smallest in A by A.popleft()


Complexity
Time O(nlogn)
Space O(n)

"""
from typing import List
from collections import deque

class Solution:
    def advantageCount(self, A, B):
        A = deque(sorted(A))
        for b, i in sorted([-b, i] for i, b in enumerate(B)):
            B[i] = A.pop() if -b < A[-1] else A.popleft()
        return B


s = Solution()
print(s.advantageCount([2,7,11,15], [1,10,4,11]))
