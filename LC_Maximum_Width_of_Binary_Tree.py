"""
662. Maximum Width of Binary Tree

Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:
Input:

           1
         /   \
        3     2
       / \     \
      5   3     9

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:
Input:

          1
         /
        3
       / \
      5   3

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:
Input:

          1
         / \
        3   2
       /
      5

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:
Input:

          1
         / \
        3   2
       /     \
      5       9
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


Note: Answer will in the range of 32-bit signed integer.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Approach:
Recurisvely do a binary search -- check level by level with positions.

Enquee node with depth and position...
when a node,depth,position is dequeue from the queue. (add children, depth+1, 2*postion) and 2*position+1 into the Queue.
while traversing the queue.. when see depth change.. not the min position.
calucalte the different between position and min position and try to maximze this.
keep doing this.. ulimtely maxval will have the answer.

"""
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        Queue = [(root, 0, 0)]
        currentdepth = None
        maxval = 0
        for (node, depth, position) in Queue:
            if (node == None):
                continue;
            Queue.append((node.left, depth+1, 2*position))
            Queue.append((node.right, depth+1, 2*position+1))
            if (depth != currentdepth):
                left = position
                currentdepth = depth
            # Remember the plus one becauase 1-0... should be 2
            maxval = max(maxval, position-left+1)
        return maxval
