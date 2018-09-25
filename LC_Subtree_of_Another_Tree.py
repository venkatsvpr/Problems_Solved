"""
572. Subtree of Another Tree

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
 return false
 """
 # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Have a helper function to check equality.
if  s != None and ( if s,t is equal else check subtree exists on s.left and s.right)
"""
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def equals (s, t):
            if (s == None) and (t == None):
                return True
            if (s == None) or (t == None):
                return False
            if (s.val == t.val and equals(s.left,t.left) and equals(s.right, t.right)):
                return True
            return False
        # check if a match exists a this point or check on left and right side with t
        if (s != None) and (equals(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)):
            return True
        return False
