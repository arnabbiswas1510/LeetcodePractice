"""
https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/
"""

from collections import defaultdict
import math
class Solution:
    def restoreArray(self, adjacentPairs):
        adj, ans, n = defaultdict(list), [], len(adjacentPairs) + 1
        for a, b in adjacentPairs:
            adj[a] += [b]
            adj[b] += [a]
        prev = -math.inf
        for k, v in adj.items():
            if len(v) == 1:
                ans += [k]
                break
        while len(ans) < n:
            for next in adj.pop(ans[-1]):
                if next != prev:
                    prev = ans[-1]
                    ans += [next]
                    break
        return ans


s = Solution()
print(s.restoreArray([[2,1],[3,4],[3,2]]))
