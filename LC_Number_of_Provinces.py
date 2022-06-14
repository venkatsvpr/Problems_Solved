"""
547. Number of Provinces

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        root = [i for i in range(len(isConnected))]
        
        # Find the root
        def find(x):
            if (x == root[x]):
                return x
            root[x] = find(root[x])
            return root[x]
        
        # Union of x and y
        def union(x,y):
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                root[rootx] = rooty
            return
        
        # Look through the connected list
        for x in range(len(isConnected)):
            for y in range(len(isConnected[0])):
                # do only for y > x:
                if isConnected[x][y] == 1 and y> x:
                    union(x,y)
        
        provinces = set()
        # Look through the root
        for i in range(len(root)):
            provinces.add(find(i))
        
        # Look for total number of provinces
        return len(provinces)
                    
            
                
                