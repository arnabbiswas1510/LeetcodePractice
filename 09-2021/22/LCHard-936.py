"""
https://leetcode.com/problems/stamping-the-sequence/

Methodical coding. Just follow through and code it out
"""


def canReplace(tList, pos, sList):
    for i in range(len(sList)):
        if tList[i + pos] != '?' and tList[i + pos] != sList[i]:
            return False
    return True

def replace(tList, pos, length):
    count=0
    for i in range(pos, pos + length):
        if tList[i] != '?':
            tList[i] = '?'
            count +=1
    return count


class Solution:
    def movesToStamp(self, stamp, target) -> str:
        tList=list(target)
        sList=list(stamp)
        count=0
        visited=[False]*len(tList)
        res=[]

        while count != len(tList):
            didChange=False
            for i in range(len(tList)-len(sList)+1):
                if not visited[i] and canReplace(tList, i, sList):
                    count += replace(tList, i, len(sList))
                    visited[i]=True
                    didChange=True
                    res.append(i)
                    if count == len(tList):
                        break

            if not didChange:
                return None

        for i in range(len(res)//2):
            res[i], res[len(res)-(i+1)] = res[len(res)-(i+1)], res[i]
        return res


s = Solution()
print(s.movesToStamp("abca", "aabcaca"))
