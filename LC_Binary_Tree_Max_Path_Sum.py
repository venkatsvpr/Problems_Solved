"""
124. Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Approach:
At every node we compute two things.. best terminating at me.. best going up
best below me = max (left.terminating, right.terminating, right_up, left_up)
best terminating at me = left.going_up + right.going up + myvalue
best going up  = max(myvale, max(left.going up,right.going up)+myvalue )
return best_below_me, best_terminating_at_me, best going_up
and push this value up.
"""
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def rec_call (root):
            if (root == None):
                return [0, 0, 0]
            if (root.right == None) and (root.left == None):
                return [root.val, root.val, root.val]
            left_below = left_terminate = left_up = right_below = right_terminate = right_up = float('-inf')
            if (root.left != None):
                [left_below, left_terminate, left_up] = rec_call (root.left)
            if (root.right != None):
                [right_below, right_terminate, right_up] = rec_call (root.right)

            best_below = max(left_below, right_below, left_terminate, right_terminate,right_up,left_up)
            best_terminate =max(root.val, root.val + left_up + right_up)
            best_up = max(root.val ,root.val + max(left_up,right_up))
            return [best_below, best_terminate, best_up]
        return (max(rec_call(root)))
