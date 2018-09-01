"""
669. Trim a Binary Search Tree


Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

Example 1:
Input:
    1
   / \
  0   2

  L = 1
  R = 2

Output:
    1
      \
       2
Example 2:
Input:
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output:
      3
     /
   2
  /
 1


"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Approach is very simple..
1) if i have range that is spreading over me..  i ask my left and right subtree if there is a match.
add all the values with mine and send it up
2) if the range is to my left.. call only for left and return the value.. dont include me
3) if the range is to my right.. call only for the right and return the value.. dont include me
4) do this recursively
"""
class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if (root == None):
            return None
        if (L <= root.val) and (root.val <= R):
            retL = self.trimBST (root.left, L, root.val)
            retR = self.trimBST (root.right, root.val, R)
            root.left  = retL
            root.right = retR
            return root
        elif ( L > root.val):
            return self.trimBST (root.right, L, R)
        elif ( R < root.val):
            return self.trimBST (root.left, L, R)
