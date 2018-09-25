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
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Approach:
Start from the root and go till leaf ..
check if the sum is equal to the required sum and we are at the leaf node
and add the path to the Answer.

If all numbers will be positive. then we can stop in the middle.
else if negative numbers are also there we cannot stop
"""
class Solution(object):
    def pathSum(self, root, s2):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def recSum (past, node, s, Ans):
            if (node == None):
                return
            pastsum = sum(past)
            if (pastsum + node.val == s) and (node.left == None) and (node.right == None):
                Ans.append(past[:]+[node.val])
            recSum (past + [node.val], node.left, s, Ans)
            recSum (past + [node.val], node.right, s, Ans)
            return
        Past = []
        Ans = []
        recSum (Past, root, s2, Ans)
        return Ans
