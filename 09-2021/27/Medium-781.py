"""
https://leetcode.com/problems/rabbits-in-forest/
"""


import math
class Solution:
    def numRabbits(self, ans) -> int:
        d={}
        #Generate frequency dict of all answers
        for i in ans:
            if(d.get(i)!=None):
                t=d.get(i)
                t+=1
                d[i]=t
            else:
                d[i]=1

        fans=0
        for k in d.keys():
            tt=(k+1)*math.ceil(d[k]/(k+1))
            fans+=tt
        return fans
