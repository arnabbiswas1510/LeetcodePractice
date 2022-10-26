"""
https://leetcode.com/problems/isomorphic-strings/

Explanation:

First instinct was to compare two frequency counts. But this would not have worked since you are comparing here that the
mapping is the same

"""
from typing import List


class Solution:
    def isIsomorphic(self, s:str, t:str) -> bool:
        mapST, mapTS = {}, {}
        for c1, c2 in zip(s,t):
            if ((c1 in mapST and mapST[c1] != c2) or
                (c2 in mapTS and mapTS[c2] != c1)):
                return False
            mapST[c1] =c2
            mapTS[c2] = c1
        return True

    #more concise version
    def isIsomorphic2(self, s:list, t:list) -> bool:
        mapST, mapTS = {}, {}
        for i in range(len(s)):
            if s[i] in mapST and t[i] in mapTS and mapST[s[i]] != mapTS[t[i]]: #Bug here, need to initialize map with 0
                # values instead. Or use defaultDict
                return False
            mapST[s[i]] =i+1
            mapTS[t[i]] = i+1
        return True

s = Solution()
print(s.isIsomorphic2(list("egg"), list("axd")))
