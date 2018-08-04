"""
337. House Robber III


The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Approach:
At every level return two values
value[0] =  the best with current val ... current_val + leftsidewithout + rightside_Without
value[1] =  the best without me... max(leftwith  + left_without) + max(rightwith + rightwithout)
"""
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def rec (root):
            if (root == None):
                return 0,0
            l1,l2 = rec(root.left)
            r1,r2 = rec(root.right)
            ret1 = root.val+l2+r2
            # Best of value without me.. involves. best of without my child + best of with my child
            # on both sides
            ret2 = max(l1,l2) + max(r1,r2)
            return ret1,ret2
        return max(rec(root))
