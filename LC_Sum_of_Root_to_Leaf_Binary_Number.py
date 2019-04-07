"""
1022. Sum of Root To Leaf Binary Numbers

Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.

 

Example 1:



Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
 

Note:

The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
The answer will not exceed 2^31 - 1.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Start from root. 
multiply whatever you get by 2 add current value and send it down.
keep adding answers
"""
class Solution:
    def __init__(self):
        self.Ans = 0
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def rec (root, val):
            val *= 2
            val += root.val
            if (root.right is None and root.left is None):
                self.Ans += val
                return
            if (root.left):
                rec (root.left,  val)
            if (root.right):
                rec (root.right, val)
        rec (root, 0)
        return int(self.Ans)
                
        
