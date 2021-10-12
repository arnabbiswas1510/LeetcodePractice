"""
https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/

Explanations:
https://www.youtube.com/watch?v=4OL7WdGKC1Y
https://www.youtube.com/watch?v=a9-NtLIs1Kk
"""
from typing import List


class Solution:
    def findIntegers(self, n: int) -> int:
        # f stores the fibonacci numbers
        f = [1, 2]
        for i in range(2, 30):
            f.append(f[-1]+f[-2])

        # last_seen tells us if there was a one right before.
        # If that is the case, we are done then and there!
        # ans is the answer
        ans, last_seen = 0, 0
        for i in reversed(range(30)):
            if (1 << i) & n: # is the ith bit set? Mem
                ans += f[i]
                if last_seen:
                    ans -= 1
                    break
                last_seen = 1
            else:
                last_seen = 0
        return ans+1 #Mem: add 1 to include current word


s = Solution()
print(s.findIntegers(5))
