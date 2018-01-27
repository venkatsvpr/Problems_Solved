# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
Do level order traversal. Save the average of the levels
Return it as the answer
"""
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        current_nodes = []
        
        if root is None:
            return
        Answer = []
        current_nodes.append(root)
        while (current_nodes):
            future_nodes = []
            count = 0
            total = 0
            for element in current_nodes:
                if element is None:
                    continue;
                else:
                    count = float(count+1)
                    total = float(total+element.val)
                    future_nodes.append(element.left)
                    future_nodes.append(element.right)
            if (count >0):
                Answer.append(total/count)
            current_nodes = future_nodes
        return Answer
        
        
