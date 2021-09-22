"""
https://leetcode.com/problems/integer-to-roman/
"""

from bisect import bisect

class Solution:
    def intToRoman(self, num: int) -> str:

        # Make hasmap to handle integer to string
        romans = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
                  40: "XL", 50: "L", 90: "XC", 100: "C",
                  400: "CD", 500: "D", 900: "CM", 1000: "M"}

        # Store all the keys in sorted order
        k = list(sorted(romans.keys()))

        # Loop till a specific condition met
        s = ""
        while True:

            # Get the index in k, s.t., that
            # value can be subtracted from num
            i = bisect(k, num) - 1

            # If index is out of bound, break
            if i < 0:
                break
            else:

                # Get the value to subtract from num
                v = k[i]

                # update num
                num = num - v

                # Append to string, w.r.t, the value subtracted from num
                s = s + romans[v]

        return s # return the string

s= Solution()
print(s.intToRoman(509))