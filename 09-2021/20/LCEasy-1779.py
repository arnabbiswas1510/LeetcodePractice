"""
https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/
"""

class Solution:
    def nearestValidPoint(self,x,y,points):
        res, dist = 99**99, 99**99
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                currDist = abs(x - points[i][0]) + abs(y - points[i][1]) #Manhattan distance
                if currDist < dist:
                    dist = currDist
                    res = i
        return -1 if res == 99**99 else res

s=Solution()
print(s.nearestValidPoint(3,4,[[1,2],[3,1],[2,4],[2,3],[4,4]]))
