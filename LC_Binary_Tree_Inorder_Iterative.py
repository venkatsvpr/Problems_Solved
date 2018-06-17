"""
94. Binary Tree Inorder Traversal
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        st = []
        Ans = []
        node = root
        while ((len(st) > 0)  or (node!=None)):
            if (node != None):
                st.append(node)
                node = node.left
            else:
                Ans.append(st[-1].val)
                node = st[-1].right
                st.pop()
        return Ans
