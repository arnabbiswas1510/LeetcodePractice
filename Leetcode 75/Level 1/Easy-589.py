"""
https://leetcode.com/problems/n-ary-tree-preorder-traversal/

Explanation:

"""
from typing import List

"""
Recursive Solution: 


# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        output =[]

        # perform dfs on the root and get the output stack
        self.dfs(root, output)

        # return the output of all the nodes.
        return output

    def dfs(self, root, output):

        # If root is none return
        if root is None:
            return

        # for preorder we first add the root val
        output.append(root.val)

        # Then add all the children to the output
        for child in root.children:
            self.dfs(child, output)

"""
Iterative Solution- Always use stack and extend the list inserting in reverse order
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []

        stack = [root]
        output = []

        # Till there is element in stack the loop runs.
        while stack:

            #pop the last element from the stack and store it into temp.
            temp = stack.pop()

            # append. the value of temp to output
            output.append(temp.val)

            #add the children of the temp into the stack in reverse order.
            # children of 1 = [3,2,4], if not reveresed then 4 will be popped out first from the stack.
            # if reversed then stack = [4,2,3]. Here 3 will pop out first.
            # This continues till the stack is empty.
            stack.extend(temp.children[::-1]) #Note this step

        #return the output
        return output