"""
113. Path Sum II
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

Approach:
==========

1) Traverse through the tree.
2) If sum is greater than expected. .stop at that point.
3) if equal add the path to the Answer
4) If sum is less traverse to left and right
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, expected):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def rec (root, past, Ans, S):
            if (root == None):
                return
            new_sum = root.val + sum(past)
            if (new_sum > S):
                return

            # If the sum is equal to the expected. add it to Answer
            if (new_sum == S):
                past.append(root.val)
                Ans.append(past[:])
                past.pop()
                return

            # If new_sum is less than S continue with left and right
            past.append(root.val)
            rec (root.left, past, Ans, S)
            rec (root.right, past, Ans, S)
            past.pop()
            return

        Ans = []
        S = expected
        past = []
        rec (root, past, Ans, S)
        return Ans
