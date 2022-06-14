"""
286. Walls and Gates


You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

 

Example 1:


Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Example 2:

Input: rooms = [[-1]]
Output: [[-1]]
 

Constraints:

m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 231 - 1.
"""

import queue 
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        # First identify the gateys
        # Perform bfs from there and spread the distance
        
        def findGates(rooms):
            gates = []
            for i in range(len(rooms)):
                for j in range(len(rooms[0])):
                    if rooms[i][j] == 0:
                        gates.append([i,j])
            return gates
        def findNext(x,y):
            possibleNext = [ (x+1, y) , (x-1, y), (x, y+1), (x, y-1)]
            nxts = []
            for (x1,y1) in possibleNext:
                if (x1 < 0 or y1 <0 or x1 >= len(rooms) or y1 >= len(rooms[0])):
                    continue
                if rooms[x1][y1] == 2147483647:
                    nxts.append((x1,y1))
            return nxts
        q = queue.Queue()
        for [x,y] in findGates(rooms):
            q.put((x,y))
        
        # Perform BFS 
        while(q.qsize() > 0):
            (x1,y1) = q.get()
            for (x2,y2) in findNext(x1,y1):
                rooms[x2][y2] = rooms[x1][y1] +1
                q.put((x2,y2))
        return
        
               
        