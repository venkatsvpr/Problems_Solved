# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        Ans = []
        level = [root]
        count = 0
        while root and level:
            Current = []
            Child = []
            for item in level:
                if (count %2 == 0):
                    Current.append(item.val)
                else:
                    Current.insert(0,item.val)
                if (item.left):
                    Child.append(item.left)
                if (item.right):
                    Child.append(item.right)
            Ans.append(Current)
            level = Child
            count += 1
        return Ans
   
