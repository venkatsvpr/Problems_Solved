"""
863. All Nodes Distance K in Binary Tree


We are given a binary tree (with root node root), a target node, and an integer value `K`.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.



Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
Output: [7,4,1]
Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.

Note:

    The given tree is non-empty.
    Each node in the tree has unique values 0 <= node.val <= 500.
    The target node is a node in the tree.
    0 <= K <= 1000.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Logic is to search through the nodes till we find the target.
# Issue search for left and right subtree and for the parent
class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[TreeNode]
        """
        # Recursively traverse through the node down for k nodes.
        # Add the Answer to the Ans when k==0
        def rec_traverse (node, k,Ans):
            if (node == None):
                return
            if (k == 0):
                Ans.append(node.val)
                return
            else:
                rec_traverse (node.left, k-1, Ans)
                rec_traverse (node.right, k-1, Ans)

        # Search till find the target.
        def rec_search (root, target,Ans,k):
            #print (root.val,Ans,target)
            if (root == None):
                return -1
            if (target.val == root.val):
                rec_traverse(root, k, Ans)
                return k-1
            v1 = v2 = 0
            v1 = rec_search (root.left, target,Ans,k)
            if (v1 > 0):
                rec_traverse(root.right, v1-1, Ans)
            elif (v1 == 0):
                rec_traverse(root, 0, Ans)
            else:
                v2 = rec_search (root.right, target,Ans,k)
                if (v2 > 0):
                    rec_traverse(root.left,v2-1,Ans)
                elif (v2 == 0):
                    rec_traverse(root,v2,Ans)

            return max(v1,v2)-1
        Ans = []
        rec_search(root,target,Ans,K)
        return Ans
