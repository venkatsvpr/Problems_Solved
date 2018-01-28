# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
1) If both p&q are on the left/right. move left/right
2) If one is on left and other on the right. return the current_node
3) if current node is equal to p/q. return current_node
"""
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def rec_find (root, p, q):
            if (root is None):
                return root
            elif ((root.val == p.val) or (root.val == q.val)):
                return root
            elif ((root.val < p.val) and (root.val <q.val)):
                return (rec_find (root.right, p, q))
            elif ((root.val > p.val) and (root.val >q.val)):
                return (rec_find (root.left, p, q))
            else:
                return root;
        return (rec_find(root,p,q))
        
        
