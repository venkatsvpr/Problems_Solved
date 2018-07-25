"""
110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def rec_traverse (node):
            if (node == None):
                return [True, 0]
            left = rec_traverse(node.left)
            right = rec_traverse(node.right)
            if (left[0]== False) or (right[0] == False):
                return [False,-1]
            if (abs(left[1]-right[1]) > 1):
                return [False,-1]
            else:
                return [True,1+max(left[1],right[1])]
        retval = rec_traverse(root)
        if (retval[0] == True):
            return True
        return False
