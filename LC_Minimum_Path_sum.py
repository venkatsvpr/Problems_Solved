"""
64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

Simple dp

"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def rec (grid, dp, x, y, m , n):
            if (x >= m):
                return float('inf')
            if (y >= n):
                return float('inf')
            if (x == m-1) and (y == n-1):
                dp[x][y] = grid[x][y]
                return grid[x][y]
            if (dp[x][y] > 0):
                return dp[x][y]
            dp[x][y] =  grid[x][y] + min (rec(grid, dp, x+1,y, m,n), rec(grid,dp,x,y+1,m,n))
            return dp[x][y]
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n) ]  for j in range(m)]
        rec (grid, dp, 0, 0, m, n)
        return dp[0][0]
