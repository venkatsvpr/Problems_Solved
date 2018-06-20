"""
449. Serialize and Deserialize BST

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Approach: Do an inorder traversal using Stacks
# Reconstruct the tree by using the property of the binary search tree
# We are inserting right followed by left because. while popping left comes first.
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if (root is None):
            return []
        St = []
        St.append(root)
        Ans = []
        # Inorder traversal
        while(len(St)>0):
            item = St.pop()
            Ans.append(item.val)
            if (item.right != None):
                St.append(item.right)
            if (item.left  != None):
                St.append(item.left)

        return Ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        # We are passing Stack as argument because they are mutable.
        def insert (left, right, St):
            if (len(St) == 0):
                return None
            if ( left < St[0]) and (St[0]  < right):
                root = TreeNode(St.pop(0))
                root.left = insert(left,root.val,St)
                root.right = insert(root.val, right,St)
                return root
        return insert(float('-inf'),float('inf'),data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
