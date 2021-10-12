"""
https://leetcode.com/problems/flatten-nested-list-iterator/
"""
from typing import List


class NestedIterator(object):

    def __init__(self, nestedList):
        self.stack = [[nestedList, 0]]

    def next(self):
        if self.hasNext():
            nestedList, i = self.stack[-1]
            self.stack[-1][1] += 1
            return nestedList[i]
        else:
            return None

    def hasNext(self):
        s = self.stack
        while s:
            nestedList, i = s[-1]
            if i == len(nestedList):
                s.pop()
            else:
                x = nestedList[i]
                if isinstance(x, int):
                    return True
                s[-1][1] += 1
                s.append([x, 0])
        return False


s = NestedIterator([1,[1,1],2,[1,1]])
print(s.next())
print(s.next())
print(s.next())
print(s.next())
print(s.next())
print(s.next())
