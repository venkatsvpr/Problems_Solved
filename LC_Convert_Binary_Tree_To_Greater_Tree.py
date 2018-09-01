"""
538. Convert BST to Greater Tree


iven a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Define a recursive function. defaultly call it with zero
At every node.. call the rightwith that default value.. whatever right returns.. store it
add the right retunred value + defaultly called value  to root.val.
call left withsum of passd from up + left return + root.val as default value.
return summ of me..right return + left return  + myvalue
"""
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def recT (root, val):
            if (root == None):
                return 0
            rightReturn = recT (root.right, val)
            root.val = root.val + rightReturn + val
            leftReturn = recT (root.left, root.val)
            return root.val + leftReturn - val
        recT (root, 0)
        return root



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Call right..
add the rootvalue to total.
update the root.value  to total value
call for left
"""
class Solution(object):
    def __init__ (self):
        self.total = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if (root is None):
            return None
        self.convertBST (root.right)
        self.total += root.val
        root.val = self.total
        self.convertBST (root.left)
        return root
