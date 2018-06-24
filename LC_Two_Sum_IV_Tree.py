"""
653. Two Sum IV - Input is a BST

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True

Example 2:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        # Have a hash map to store the expected value
        # traverse the treee.
        """
        def traverse (root):
            if (root == None):
                return False
            if (root.val in ToFind):
                return True
            #print (ToFind)
            ToFind[k-root.val] = True
            if (True == traverse (root.left)):
                return True
            if (True == traverse (root.right)):
                return True
            return False
        ToFind = dict()
        if (True == traverse(root)):
            return T  rue
        return False
