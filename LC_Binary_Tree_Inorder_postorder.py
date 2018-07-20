"""
106. Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
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
pop from the end. get the element.
find the index of the element in inorder and then recursively call.
parse right first and then left.


"""
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def recall (inorder, postorder, start , end):
            #print (" start,end ",start,end)
            if (start >= end) or (len(postorder) == 0):
                return None
            node = TreeNode(postorder.pop())
            idx = inorder[start:end].index(node.val)
            node.right = recall(inorder, postorder, start+idx+1, end)
            node.left = recall(inorder, postorder, start, start+idx)
            return node
        return (recall(inorder, postorder, 0, len(postorder)))
