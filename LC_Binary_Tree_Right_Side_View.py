"""
199. Binary Tree Right Side View


Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

"""# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Approach;
Very simple problem.. call left and then right..
the right most node will be called at last and it will udpate the dictionary.
which will hold the right most value.


We could also do a level order traversal and get the right most value
"""
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def rec (root, d , depth):
            if (root == None):
                return
            d [depth]  = root.val
            rec(root.left, d, depth+1)
            rec(root.right, d, depth+1)
        hashMap = dict()
        rec (root, hashMap, 0)
        Ans = [hashMap[key] for key in hashMap]
        return Ans


        
