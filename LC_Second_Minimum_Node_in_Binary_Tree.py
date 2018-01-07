# Second Minimum Node in Binary Tree
# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [float('inf')]
        def rec_traverse (node):
            if (not node):
                return;
            if root.val < node.val < res[0]:
                res[0] = node.val
            rec_traverse (node.left)
            rec_traverse (node.right)
        
        rec_traverse(root)
        if (res[0] == float('inf')):
            return -1;
        else:
            return res[0]
