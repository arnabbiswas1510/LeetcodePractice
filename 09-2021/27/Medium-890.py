"""
https://leetcode.com/problems/find-and-replace-pattern/
"""


def di(p):
    a=[]
    b=[]
    for i in p:
        if i not in b:
            a.append(p.index(i))
            b.append(i)
        else:
            a.append(b.index(i))
    return a
class Solution:
    def findAndReplacePattern(self, words, pattern):
        b=di(pattern)
        a=[]
        for i in words:
            if di(i)==b:
                a.append(i)
        return a

s = Solution()
print(s.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "aee"))
