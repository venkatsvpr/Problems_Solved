"""
1382. Balance a Binary Search Tree

Given a binary search tree, return a balanced binary search tree with the same node values.

A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.

 

Example 1:



Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.
 

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The tree nodes will have distinct values between 1 and 10^5.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Logic:
1) Do Inorder traversal and get all the elements in increasing order
2) Build the BST from the middle element
"""
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        valueList = []
        def dfs(node):
            if node:
                dfs(node.left)
                valueList.append(node.val)
                dfs(node.right)
        
        def rebuild (lt):
            if not lt:
                return None
            midElement = len(lt)/2
            root = TreeNode(lt[midElement])
            root.left = rebuild(lt[:midElement])
            root.right = rebuild(lt[midElement+1:])
            return root
            
        dfs(root)
        return rebuild(valueList)