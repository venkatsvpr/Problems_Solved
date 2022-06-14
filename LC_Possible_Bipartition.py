"""
890. Possible Bipartition
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group.

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.



Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false


Note:

1 <= N <= 2000
0 <= dislikes.length <= 10000
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].
"""

"""
Approach: This is a bi-partite graph testing problem
color a node as 1.. all of its neightbours should  be 2..or un-set
if any of the neighbour is 1.. then the graph cant be bipartite.
"""
class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        # perform dfs
        def dfs (node, color,graph, c):
            # If we have already seen the node, check if it is colored properly
            if (node in color):
                if (color[node] != c):
                    return False
                else:
                    return True
            
            # color the node if we have not seen it
            color[node] = c
            
            allTrue = True
            for nxt in graph[node]:
                if False == dfs(nxt, color, graph , not c):
                    allTrue = False
            return allTrue
        
        ## Construct the adjaceny map
        graph = collections.defaultdict(list)
        for [u,v] in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        ## colors
        color = dict() 
        for i in range(1,N+1):
            if (i not in color):
                if (False == dfs(i,color,graph,True)):
                    return False
        return True