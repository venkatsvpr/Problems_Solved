# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Visit Level by level. Store the current nodes visited in the answers.
Then navigate the next child level
"""
class Solution:
    def levelOrder(self, root):
        Ans = []
        level = [root]
        while root and level:
            Current = []
            Child = []
            for item in level:
                Current.append(item.val)
                if (item.left):
                    Child.append(item.left)
                if (item.right):
                    Child.append(item.right)
            Ans.append(Current)
            level = Child           
        return Ans
   
