# Number of Islands
# https://leetcode.com/problems/number-of-islands/description/
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = 0
        m = len(grid)
        if (m >0):
            n = len(grid[0])
        
        
        def modified_dfs (i,j):
            if ((0<=i<m) and (0<=j<n) and (grid[i][j]== "1")):
                grid[i][j] = 0
                modified_dfs (i-1 , j)
                modified_dfs (i+1 , j)
                modified_dfs (i, j+1)
                modified_dfs (i, j-1)
                return 1
            else:
                return 0
        
       
        if (m == n):
            if (n == 0):
                return 0

        
        num_of_islands = [modified_dfs(i,j) for i in range(m) for j in range(n) if grid[i][j]]
        return sum(num_of_islands)
