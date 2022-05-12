"""
417. Pacific Atlantic Water Flow


There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Example 2:

Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105


We start the left, right, top, bottom edge - Pick point and then go to neighbors which are not visited
    which are newpoints >= current point, So that water can flow from newpoint to current point
Track the visited points
Go through the i,j , recursively mark a node as visited and look at neighburs.


"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacVisit = [[False for i in range(len(heights[0]))] for j in range(len(heights))]
        atVisit = [[False for i in range(len(heights[0]))] for j in range(len(heights))]
        def getNeighbors(x,y):
            # Get neighbors. consider all valid points and water has to flow to here from the neighbour so  heights[neighbors] >= heights [current]
            n = [[x-1,y], [x+1,y], [x,y-1], [x, y+1]]
            good = list()
            for item in n:
                if item[0] >= 0 and item[0] < len(heights) and item[1] >=0 and item[1] < len(heights[0]):
                    if heights[x][y] <= heights[item[0]][item[1]]:
                        good.append(item)
            return good
        
        def recMark(x,y, typ):
            if (typ == "A"):
                atVisit[x][y] = True
                nxt = getNeighbors(x, y)
                for pt in nxt:
                    if not atVisit[pt[0]][pt[1]]:
                        recMark(pt[0], pt[1], typ)
            elif (typ == "P"):
                pacVisit[x][y] = True
                nxt = getNeighbors(x, y)
                for pt in nxt:
                    if not pacVisit[pt[0]][pt[1]]:
                        recMark(pt[0], pt[1], typ)
            return
        
        #loop through all points
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                # top and left edge
                if i == 0 or j == 0:
                    recMark(i, j, "P")
                # bottom and right edge
                if i == len(heights)-1 or j == len(heights[0])-1:
                    recMark(i, j, "A")
        Ans = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                # If visited by atlantic and pacific is set consider it as an answer
                if atVisit[i][j] and pacVisit[i][j]:
                    Ans.append([i,j])
        return Ans
                    
        
                
            