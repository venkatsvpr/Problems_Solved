"""
778. Swim in Rising Water
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

 

Example 1:


Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:


Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 50
0 <= grid[i][j] < n2
Each value grid[i][j] is unique.
"""
class Solution:
    # We would like to perform a modified BFS 
    # (where we visit points based on their height (priority queue instead of queue)
    def swimInWater(self, grid: List[List[int]]) -> int:
        def getNext(r,c):
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            nxtPoints = []
            for [dr, dc] in dirs:
                if r+dr < 0 or c+dc < 0 or r+dr >= len(grid) or c+dc >= len(grid[0]):
                    continue
                nxtPoints.append([r+dr, c+dc])
            return nxtPoints
        
        # Ensure we don't visit same point twice
        visited = set()
        nxtPoints = [(grid[0][0], 0, 0)] # (time, r, c)
        visited.add((0,0))
        
        while(len(nxtPoints)):
            (t,x,y) = heapq.heappop(nxtPoints) # height, r, c
            
            if x == len(grid)-1 and y == len(grid[0])-1:
                return t
            
            for [x1,y1] in getNext(x,y):
                if (x1,y1) in visited:
                    continue
                
                visited.add((x1,y1))
                heapq.heappush(nxtPoints, (max(t, grid[x1][y1]), x1, y1))
