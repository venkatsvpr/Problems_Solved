"""
866. Smallest Subtree with all the Deepest Nodes
Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.

A node is deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is that node, plus the set of all descendants of that node.

Return the node with the largest depth such that it contains all the deepest nodes in it's subtree.



Example 1:

Input: [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation:



We return the node with value 2, colored in yellow in the diagram.
The nodes colored in blue are the deepest nodes of the tree.
The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
Both the input and output have TreeNode type.
Note:

The number of nodes in the tree will be between 1 and 500.
The values of each node are unique.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode

        Recursively traverse left and right:
        return the depth and the node.
        If left depth > right depth.. the sub-tree root we are searching is on the left side. so return that
        if rightdepth > left depth.. the subtree that we are searching for is on on the right side.
        else if left depth == right_Depth
        return the current node with the +1 of the left or right depth.
        """
        def rec_t (node, depth):
            if (node is None):
                return None,depth
            left = rec_t (node.left, depth)
            right = rec_t (node.right, depth)
            if (left[1] > right[1]):
                return left[0],left[1]+1
            elif (left[1] < right[1]):
                return right[0],right[1]+1
            else:
                return node,  left[1]+1
        nd,dp = rec_t(root,0)
        return nd
