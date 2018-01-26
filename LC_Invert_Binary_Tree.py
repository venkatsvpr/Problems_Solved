# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
https://leetcode.com/problems/invert-binary-tree/description/
Swap left and right. continue doing that all throught the node
"""
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def rec_inv (root):
            if (root is None):
                return
            root.left , root.right = root.right, root.left
            rec_inv (root.left)
            rec_inv (root.right)
            return (root)
        
        return(rec_inv (root))
