"""
https://leetcode.com/problems/merge-two-sorted-lists/

Explanation:

How to solve in Space: O(1)?
"""
from typing import List

class ListNode:
    def __init__(self, dataval=None):
        self.val = dataval
        self.next = None

def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next

def printList(node):
    while node:
        print(node.val, end=", ")
        node = node.next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1 or list2:
            cur.next = list1 if list1 else list2
        return dummy.next


s = Solution()
printList(s.mergeTwoLists(lst2link([1,2,4]), lst2link([1,3,4])))
