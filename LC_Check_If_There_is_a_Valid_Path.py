"""
5366. Check if There is a Valid Path in a Grid

Given a m x n grid. Each cell of the grid represents a street. The street of grid[i][j] can be:
1 which means a street connecting the left cell and the right cell.
2 which means a street connecting the upper cell and the lower cell.
3 which means a street connecting the left cell and the lower cell.
4 which means a street connecting the right cell and the lower cell.
5 which means a street connecting the left cell and the upper cell.
6 which means a street connecting the right cell and the upper cell.


You will initially start at the street of the upper-left cell (0,0). A valid path in the grid is a path which starts from the upper left cell (0,0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

Notice that you are not allowed to change any street.

Return true if there is a valid path in the grid or false otherwise.

 

Example 1:


Input: grid = [[2,4,3],[6,5,2]]
Output: true
Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).
Example 2:


Input: grid = [[1,2,1],[1,2,1]]
Output: false
Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)
Example 3:

Input: grid = [[1,1,2]]
Output: false
Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
Example 4:

Input: grid = [[1,1,1,1,1,1,3]]
Output: true
Example 5:

Input: grid = [[2],[2],[2],[2],[2],[2],[6]]
Output: true
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
1 <= grid[i][j] <= 6

"""

"""
Do simple recursive path traversal by keeping track of visisted.
If we reach the end then we have succeeded
"""
from collections import defaultdict
class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        visited = defaultdict(bool)
        m = len(grid) - 1
        n = len(grid[0]) - 1
        """ This method will say if a point is valid """
        def isValid(x,y):
            if (x < 0 or x > m or y < 0 or y > n):
                return False
            return True
            
        """ This method wills ay if x1,y1 can join with x2,y2 """
        def CanJoin(x1,y1, x2,y2):
            if (grid[x1][y1] == grid[x2][y2]):
                return True
            if (grid[x1][y1] == 1 and grid[x2][y2] not in {2}):
                return True
            if (grid[x1][y1] == 2 and grid[x2][y2] not in {1}):
                return True
            if (grid[x1][y1] in {3, 4, 5, 6}):
                return True
            return False
        
        """ This will blindly return the two possible paths"""
        def getNext(x,y):
            if (grid[x][y] == 1):
                return [[x,y-1], [x, y+1]]
            if (grid[x][y] == 2):
                return [[x+1, y], [x-1,y]]
            if (grid[x][y] == 3):
                return [[x+1, y], [x, y-1]]
            if (grid[x][y] == 4):
                return [[x+1, y], [x, y+1]]
            if (grid[x][y] == 5):
                return [[x-1, y], [x, y-1]]
            if (grid[x][y] == 6):
                return [[x-1, y], [x, y+1]]
        def recTraverse (x,y):
            if (visited[(x,y)]):
                return False
            #print (x,y,grid[x][y],visited)
            if (x == m and y == n):
                visited[(x,y)] = True
                return True
            NextPoints = getNext(x,y)
            #print ("nxtPoints",NextPoints)
            visited[(x,y)] = True
            for lt in NextPoints:
                if (isValid(lt[0], lt[1])):
                    if (True == CanJoin(x,y,lt[0],lt[1]) and True == recTraverse(lt[0], lt[1])):
                        visited[(x,y)] = True
                        return True
            return False
        #print (m,n)
        if (True == recTraverse(0,0)):
            return True
        return False
            