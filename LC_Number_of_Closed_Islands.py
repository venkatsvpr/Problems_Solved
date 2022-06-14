"""

1254. Number of Closed Islands

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
"""
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = dict()
        def rec(x,y):
            if grid[x][y] ==1 :
                return True
            if x == 0 or x == len(grid)-1 or y == 0 or y == len(grid[0])-1:
                return False
            grid[x][y] = 1
            l= rec(x+1,y)
            r= rec(x-1,y)
            u= rec(x, y+1)
            d= rec(x, y-1)
            return  l and r and u and d
        numIslands = 0
        for x in range(1,len(grid)-1):
            for y in range(1,len(grid[0])-1):
                if grid[x][y] == 0 and rec(x,y):
                    numIslands += 1
        return numIslands