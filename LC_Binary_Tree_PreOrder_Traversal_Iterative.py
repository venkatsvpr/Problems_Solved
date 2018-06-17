"""
144. Binary Tree Preorder Traversal

Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def it_r(root):
            if (root is None):
                return []
            St = []
            St.append(root)
            while (len(St) > 0):
                node = St.pop()
                Ans.append(node.val)
                if (node.right != None):
                    St.append(node.right)
                if (node.left != None):
                    St.append(node.left)
        Ans = []
        it_r(root)
        return (Ans)

        
