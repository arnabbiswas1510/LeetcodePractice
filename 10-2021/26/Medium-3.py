"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Explanation:
https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/347818/Python3%3A-sliding-window-O(N)-with-explanation
"""
from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        output = 0
        for r in range(len(s)):
            """
            If s[r] not in seen, we can keep increasing the window size by moving right pointer
            """
            if s[r] not in seen:
                output = max(output,r-l+1)
            else:
                """
                There are two cases if s[r] in seen:
                case1: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
                case2: s[r] is not inside the current window, we can keep increase the window
                """
                if seen[s[r]] < l:
                    output = max(output,r-l+1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return output


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))