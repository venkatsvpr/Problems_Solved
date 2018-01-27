# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
Do level order traversal insert in reverse order
"""
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        current_nodes = []
        
        if root is None:
            return current_nodes
        Answer = []
        current_nodes.append(root)
        while (current_nodes):
            to_print = False
            future_nodes = []
            lt = []  
            for element in current_nodes:
                if element is None:
                    continue;
                else:
                    to_print = True;
                    lt.append(element.val)
                    future_nodes.append(element.left)
                    future_nodes.append(element.right)
            if (to_print == True):
                Answer.insert(0,lt)
            current_nodes = future_nodes
        return Answer
        
        
