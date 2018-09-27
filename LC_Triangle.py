"""
120. Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
   [2],
  [3,4],
 [6,5,7],
[4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangl
Approach:

Typical dp.. store optimum values at every level in a memoise array
and use it for further checks
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        def recFunc (memo, x, y, triangle):
            if (x >= len(triangle)) or (y >= len(triangle[x])):
                return float('inf')
            if (x == len(triangle)-1) and (y < len(triangle[x])):
                return triangle[x][y]
            if((x,y) in memo):
                return memo[(x,y)]
            memo[(x,y)] = triangle[x][y] + min (recFunc(memo,x+1,y, triangle), recFunc(memo,x+1,y+1, triangle))
            return memo[(x,y)]
        memo = dict()
        return recFunc (memo, 0, 0, triangle)
