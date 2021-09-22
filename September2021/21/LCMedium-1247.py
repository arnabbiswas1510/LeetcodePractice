"""
https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

Explanation: https://youtu.be/iplciPpgL2A
"""

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if s1==s2:
            return 0
        i,cant=0,0
        z1=list(s1)
        z2=list(s2)
        c1=[[a,b] for a,b in zip(z1,z2)].count(["y","x"]) #count num of [y,x] in list
        c2=[[a,b] for a,b in zip(z1,z2)].count(["x","y"])
        cant=(c1//2)+c1%2+(c2//2)+c1%2 #See explanation for derivation of this formula
        if (c1+c2)%2==1:
            return -1
        return cant

s = Solution()
print(s.minimumSwap("xxyyxyxyxx", "xyyxyxxxyx"))
