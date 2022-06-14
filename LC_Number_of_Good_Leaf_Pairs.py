"""
1530. Number of Good Leaf Nodes Pairs


You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.

 

Example 1:


Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.
Example 2:


Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.
Example 3:

Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
Output: 1
Explanation: The only good pair is [2,5].
 

Constraints:

The number of nodes in the tree is in the range [1, 210].
1 <= Node.val <= 100
1 <= distance <= 10

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # Perform a dfs with a notion of level
        def check(node, level):
            if node==None:
                return []
            
            # If this is leaf node insert it to a list and return
            if node.left==None and node.right==None:
                k=[]
                k.append(level)
                return k
            
            # Call recursively for both left and right nodes
            lefts=check(node.left,level+1)
            rights=check(node.right,level+1)
            
            # For all the leaf nodes from the left and right 
            for left in lefts:
                for right in rights:
                    
                    # Check if the distance beteween each otheris less than or equal to distance
                    if left - level + right- level <= distance:
                        self.ans += 1
            
            # At every level, return the left and right
            return lefts + rights
        check(root,0)
        return self.ans