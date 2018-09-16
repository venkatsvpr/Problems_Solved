"""
426. Convert Binary Search Tree to Sorted Doubly Linked List


Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.

Let's take the following BST as an example, it may help you understand the problem better:





We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

The figure below shows the circular doubly linked list for the BST above. The "head" symbol means the node it points to is the smallest element of the linked list.





Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. We should return the pointer to the first element of the linked list.

The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.



"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""

"""
Approach:
recruisve function for left and right..
Each will return two pointers.. start and end.
for left .. left.end and node has to be linked
for right .. right.start and node has to be linked
return left.start an right.end to be sent up
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def rec (node):
            if (node == None):
                return None,None
            # Call for left
            left1,left2 = rec(node.left)
            if (left2):
                left2.right = node
                node.left = left2
            # Call for right
            right1,right2 = rec(node.right)
            if (right1):
                right1.left = node
                node.right = right1
            # Return the left most of left and right most of right
            if (left1 == None):
                left1 = node
            if (right2 == None):
                right2 = node
            return left1,right2

        if (root == None):
            return None
        left,right = rec (root)
        if (left):
            left.left = right
        if (right):
            right.right = left
        return left
