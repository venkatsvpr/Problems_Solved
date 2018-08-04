"""
98. Validate Binary Search Tree
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
Approach:
Call the root is in range of -inf to inf
Call for left. from -inf to current root.value and for right with root.value to inf
recurisvely keep doing it
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def rec (left, right, node):
            if (node == None):
                return True
            if (False == rec(left, node.val, node.left)):
                return False
            if (False == rec(node.val, right, node.right)):
                return False
            if (left < node.val) and (right > node.val):
                return True
            return False
        if (True ==rec(float('-inf'),float('inf'),root)):
            return True
        return False
