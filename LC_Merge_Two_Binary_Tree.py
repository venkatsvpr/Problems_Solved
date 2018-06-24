# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Recursively do traversal

class Solution:
    def merge(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        Approach:
        Recursively go through the tree and add it to the new list.
        """
        if (t1 == None):
            return t2
        if (t2 == None):
            return t1
        t1.val += t2.val
        t1.left = self.merge(t1.left, t2.left)
        t1.right = self.merge(t1.right, t2.right)
        return t1
    def mergeTrees(self, t1, t2):
        return (self.merge(t1,t2))

    
