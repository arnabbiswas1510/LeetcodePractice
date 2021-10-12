"""
https://leetcode.com/problems/data-strea-as-disjoint-intervals
"""

class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = set()

    def addNum(self, val: int) -> None:
        self.s.add(val) # set() does not maintain insertion order in Python, unlike list

    def getIntervals(self):
        ans = []
        for v in self.s:
            if v - 1 in self.s:
                continue
            else:  # find starting point of an interval
                ans.append([v])
                while v in self.s:
                    v += 1
                ans[-1].append(v-1)
            # O(n) for creating 'ans'
        ans = sorted(ans, key = lambda x: x[0])
        # O(KlogK) for sorting ans, where K is significantly smaller than n in the follow up
        return ans


summaryRanges = SummaryRanges()
summaryRanges.addNum(1)      # arr = [1]
#print(summaryRanges.getIntervals())# return [[1, 1]]
summaryRanges.addNum(3)      # arr = [1, 3]
#print(summaryRanges.getIntervals())# return [[1, 1], [3, 3]]
summaryRanges.addNum(7)      # arr = [1, 3, 7]
#print(summaryRanges.getIntervals())# return [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2)      # arr = [1, 2, 3, 7]
#print(summaryRanges.getIntervals())# return [[1, 3], [7, 7]]
summaryRanges.addNum(6)      # arr = [1, 2, 3, 6, 7]
print(summaryRanges.getIntervals())# return [[1, 3], [6, 7]]
