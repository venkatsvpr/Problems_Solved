# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        1) Start DFS on root.
        2) Go till the leaf, add item in the Answer. All leaf nodes will inser it in Answer[0], The next level will be in Answer[1]
        3) Add the Answer
        """
        Answer = [];
        def dfs(node):
            if not node:
                return 0;
            depth = max(dfs(node.left),dfs(node.right))+1
            if (len(Answer) < depth):
                Answer.append([])
            Answer[depth-1].append(node.val)
            return depth
        dfs(root)
        return (Answer)
