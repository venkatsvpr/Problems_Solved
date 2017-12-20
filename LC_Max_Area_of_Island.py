# https://leetcode.com/problems/max-area-of-island/description/ 
# Max Area of Island
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m,n = len(grid) , len(grid[0])
        
        def dfs(i,j):
            if ((0 <= i <m) and (0 <= j < n) and grid[i][j]==1 ):
                grid[i][j] = 0
                return 1 + dfs(i-1,j) + dfs (i+1,j) + dfs (i,j+1) + dfs (i,j-1)
            else:
                return 0
        
        area = [dfs(i,j) for i in range(m) for j in range(n) if grid[i][j]]
        return max(area) if area else 0
