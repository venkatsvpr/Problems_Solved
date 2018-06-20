"""
297. Serialize and Deserialize Binary Tree
DescriptionHintsSubmissionsDiscussSolution

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example:

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"

Approach:
========
This is recursive solution. for None nodes.. add # do a pre-order traversalself.
Read it out recursively in the same way.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        1
        2 3
          4 5

        def rec(node):
            if (node == None):
                lt.append("#")
            else:
                # PRE-ORDER traversal
                lt.append(str(node.val))
                rec(node.left)
                rec(node.right)
        lt = []
        rec(root)
        return ' '.join(lt)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def rec ():
            item = next(it)
            if (item == "#"):
                return None
            else:
                node = TreeNode(int(item))
                node.left = rec()
                node.right = rec()
                return node
        it = iter(data.split())
        node = rec()
        return node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
