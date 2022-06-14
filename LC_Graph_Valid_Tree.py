"""
261. Graph Valid Tree


You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

 

Example 1:


Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
 

Constraints:

1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no self-loops or repeated edges.

"""

""" 
We do union find on this, while adding two to the union if we are having the same parent then we have a loop.
If we have a loop then the graph cant be valid

"""
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        root = [i for i in range(n)]
        
        def find(x):
            if root[x] == x:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(a,b):
            root_a = find(a)
            root_b = find(b)
            ##  If we are connecting two which are already connnected. then there is a loop
            if (root_a == root_b):
                return False
            
            root[root_a] = root_b
            return True
        
        for [u,v] in edges:
            if False == union(u,v):
                return False
        
        groups = set()
        for i in range(n):
            groups.add(find(i))
        return len(groups) == 1
