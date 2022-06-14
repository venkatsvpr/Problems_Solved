"""
2096. Step-By-Step Directions From a Binary Tree Node to Another

You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.

 

Example 1:


Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
Example 2:


Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.
 

Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= n
All the values in the tree are unique.
1 <= startValue, destValue <= n
startValue != destValue

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def findAncestor(root,startValue, endValue):
            def rec(node, startValue, endValue):
                if node == None:
                    return False, None
                left, leftans = rec(node.left,startValue, endValue)
                right, rightans = rec(node.right,startValue, endValue)

                mid = (node.val == startValue) or (node.val == destValue)
                if  left + right + mid >= 2:
                    return True, node
                
                if left:
                    return left, leftans
                
                if right:
                    return right, rightans
            
                if mid:
                    return True, None
                
                return False,None
            ok,val = rec(root,startValue, endValue)
            if ok:
                return val
            return None
        def findLevel(node, start):
            if node == None:
                return float(-inf) 
            print(node.val, start)
            if (node.val == start):
                return 0
            return 1 + max(findLevel(node.left, start) , findLevel(node.right,start))
        def findDirection(node,end):
            if node == None:
                return False, ""
            if node.val == end:
                return True, ""
            left,leftPath = findDirection(node.left, end)
            if left == True:
                return True, "L"+leftPath
            
            right, rightPath = findDirection(node.right, end)
            if right == True:
                return True, "R"+rightPath
            return False, ""
        
        # Find the Lowest commmon ancestor
        ancestor = findAncestor(root, startValue, destValue)
        
        # Find the level for the start point, Sine everything would be U
        startPath = "U" * findLevel(ancestor, startValue)
        
        # Find the path for the end point, Since we 
        val,endPath = findDirection(ancestor, destValue)
        return startPath + endPath