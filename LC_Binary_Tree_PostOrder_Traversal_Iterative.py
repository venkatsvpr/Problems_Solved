"""
145. Binary Tree Postorder Traversal
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def peek(St):
            if (len(St) > 0):
                return St[-1]
            return None

        def iter (root):
            if (root is None):
                return []
            St = []
            while (True):
                while (root):
                    if (root.right != None):
                        St.append(root.right)
                    St.append(root)
                    root = root.left;
                root = St.pop()
                if  (root.right != None) and (root.right == peek(St)):
                    St.pop()
                    St.append(root)
                    root = root.right
                else:
                    Ans.append(root.val)
                    root = None
                if (len(St) <= 0):
                     return Ans
        Ans = []
        iter(root)
        return Ans

        
