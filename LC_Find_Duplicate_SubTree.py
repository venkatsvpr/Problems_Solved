"""
652. Find Duplicate Subtrees

Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4

The following are two duplicate subtrees:

      2
     /
    4

and

    4

Therefore, you need to return above trees' root in the form of a list
Approach:
==========
- Recrusively call. return (root.val)+func(left)+fun(right)
- Use this as hash and insert the node.
- whichever is having h of length greater than 1 return the first tree node from hash[0]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        def rec(root):
            if (root == None):
                return "null"
            else:
                st = str(root.val)+","+str(rec(root.left))+","+str(rec(root.right))
                h[st].append(root)
                return st

        h = collections.defaultdict(list)
        rec(root)
        Ans = []

        for key in h:
            if (len(h[key]) > 1):
                Ans.append(h[key][0])
        return Ans
