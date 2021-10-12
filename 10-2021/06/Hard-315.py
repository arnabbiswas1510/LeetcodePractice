"""
https://leetcode.com/problems/count-of-smaller-numbers-after-self/

Explanation: https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/445769/merge-sort-CLEAR-simple-EXPLANATION-with-EXAMPLES-O(n-lg-n)

Another natural choice for this problem is Segment Trees
"""
from typing import List

class SegMentTreeNode:
    def __init__(self,start,end,val,left = None,right = None):
        self.start = start
        self.end = end
        self.val = val
        self.left = left
        self.right = right

def buildTree(start,end,array):
    if start == end:
        return SegMentTreeNode(start,end,array[start])
    mid = (start+end)//2
    left = buildTree(start,mid,array)
    right = buildTree(mid+1,end,array)
    return SegMentTreeNode(start,end,left.val+right.val,left,right)

def update(node,ind,val):
    if node.start == node.end == ind:
        node.val = val
        return
    mid = (node.start + node.end)//2
    if ind>mid:
        update(node.right,ind,val)
    else:
        update(node.left,ind,val)
    node.val = node.left.val + node.right.val

def queryRange(node,start,end):
    if start>end:
        return 0
    if node.start == start and node.end == end:
        return node.val
    else:
        mid = (node.start + node.end) // 2
        if start>mid:
            return queryRange(node.right,start,end)
        elif end<=mid:
            return queryRange(node.left,start,end)
        else:
            return queryRange(node.left,start,mid)+queryRange(node.right,mid+1,end)


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr=[] # array with indexes
        res=[0]*len(nums)

        # add (num, index) tuples
        for i,num in enumerate(nums):
            arr.append((num, i))

        def merge(left, right):
            l=0
            r=0
            out=[]
            numElemsRightArrayLessThanLeftArray=0
            while l < len(left) and r < len(right):
                if left[l][0] > right[r][0]:
                    out.append(right[r])
                    r += 1
                    numElemsRightArrayLessThanLeftArray += 1
                else:
                    out.append(left[l])
                    res[left[l][1]] += numElemsRightArrayLessThanLeftArray
                    l += 1
            if l < (len(left)):
                for i in range(l, len(left)):
                    out.append(left[i])
                    res[left[i][1]] += numElemsRightArrayLessThanLeftArray
            if r < (len(right)):
                for i in range(r,len(right)):
                    out.append(right[i])
            return out

        def merge_sort(arr):
            if len(arr)==1:
                return arr
            midIndex=len(arr)//2
            left_side=merge_sort(arr[:midIndex])
            right_side=merge_sort(arr[midIndex:])
            return merge(left_side, right_side)
        _=merge_sort(arr)
        return res

    def countSmallerSegmentTree(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        sortedNums = sorted(set(nums))
        wait =  {n:i for i,n in enumerate(sortedNums)}
        freq = [0 for i in range(len(sortedNums))]
        ans = []
        root = buildTree(0,len(freq) - 1,freq)
        for n in nums[::-1]:
            freq[wait[n]] += 1
            update(root,wait[n],freq[wait[n]])
            ans.append(queryRange(root,0,wait[n]-1))
        return ans[::-1]

s = Solution()
print(s.countSmaller([5,2,6,1]))
