# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Search the level. Check the max in every level. Add it to a list. Return to a list
class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        level = [root]
        max_val = []
        while (root and level):
            Child = []
            max_item = float('-inf')
            for item in level:
                if (item.val > max_item):
                    max_item = item.val
                if (item.left):
                    Child.append(item.left)
                if (item.right):
                    Child.append(item.right)
            max_val.append(max_item)
            level = Child
        return (max_val)
        
