"""
Max Depth
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root is None):
            return 0
        return 1+ max(self.maxDepth(root.right),self.maxDepth(root.left))
        
