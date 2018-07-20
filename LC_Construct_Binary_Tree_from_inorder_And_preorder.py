"""
105. Construct Binary Tree from Preorder and Inorder Traversal
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Approach:
Use the inorder position to split the preorder and then recurisvely call
to create a binary tree.
"""
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def rec_build_tree (preorder, inorder, istart, iend):
            if (istart >= iend) or (len(preorder) == 0):
                return None
            node = TreeNode(preorder.pop(0))
            pos = inorder[istart:iend].index(node.val)
            node.left = rec_build_tree(preorder, inorder, istart, istart+pos)
            node.right = rec_build_tree(preorder, inorder, istart+pos+1, iend)
            return node
        return (rec_build_tree(preorder,inorder,0,len(preorder)))
            
