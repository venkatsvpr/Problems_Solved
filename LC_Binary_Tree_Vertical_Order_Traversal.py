"""
314. Binary Tree Vertical Order Traversal

Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
Examples 2:

Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Examples 3:

Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Have a level order traversal and when going left and right.. call left with col-1 and right col+1
have a hashmap with col number as key and node value..
go form min col to max col and output the node values
"""
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        hashMap = collections.defaultdict(list)
        mincol = maxcol = 0
        Queue = [(0, root)]
        for (col, node) in Queue:
            if (node == None):
                continue;
            mincol = min(col, mincol)
            maxcol = max(col, maxcol)
            hashMap[col].append(node.val)
            Queue.append ((col-1, node.left))
            Queue.append ((col+1, node.right))
        Ans = []
        if (0 == len(hashMap)):
            return Ans
        for key in range(mincol, maxcol+1):
            Ans.append(hashMap[key])
        return Ans

        
