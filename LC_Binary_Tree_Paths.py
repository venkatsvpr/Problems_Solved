"""
257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def rec (node, prev, Output):
            if (node == None):
                return
            prev.append(node.val)
            if ((node.right == None) and (node.left == None)):
                st = ""
                for idx,item in enumerate(prev):
                    if (idx == len(prev)-1):
                        st += str(item)
                    else:
                        st += str(item)+"->"
                Output.append(st)
            if (node.right != None):
                rec(node.right,prev,Output)
            if (node.left != None):
                rec(node.left,prev,Output)
            prev.pop()
        past = []
        Output = []
        rec (root,past,Output)
        return Output
