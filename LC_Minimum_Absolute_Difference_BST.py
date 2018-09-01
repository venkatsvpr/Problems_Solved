"""
530. Minimum Absolute Difference in BST

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
Note: There are at least two nodes in this BST.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__ (self):
        self.answer = float('inf')

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recpropagate (root, left, right):
            if (root == None):
                return
            self.answer = min (self.answer,abs(left-root.val), abs(right-root.val))
            recpropagate (root.left, left, root.val)
            recpropagate (root.right, root.val, right)

        recpropagate (root, float('-inf'), float('inf'))
        return self.answer
            
