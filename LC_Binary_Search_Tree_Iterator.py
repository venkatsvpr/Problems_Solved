"""
Binary Search Tree Iterator
https://leetcode.com/problems/binary-search-tree-iterator/description/

Insert the left subtree into a stack
When an element is popped insert the right childs left subtree 
Can achieve log(height) space.
"""
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def insert_left_node (lt, root):
    while ( root != None):
        lt.insert(0,root)
        root = root.left
    return

class BSTIterator(object):
    lt = []  
    def __init__(self, root):
        self.lt = []     
        """
        :type root: TreeNode
        """
        insert_left_node (self.lt, root)
        
    def hasNext(self):
        """
        :rtype: bool
        """
        if (0 != len(self.lt)):
            return True
        return False
        

    def next(self):
        """
        :rtype: int
        """
        if (0 == len(self.lt)):
            return 0
        
        root = self.lt.pop(0)
        insert_left_node(self.lt ,root.right)
        return root.val
        
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
