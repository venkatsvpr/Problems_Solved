"""
207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Collec the pre-requiests and hte incoming edges. 
        incoming = [0] *numCourses
        neighbors = collections.defaultdict(list)
        for a,b in prerequisites:
            incoming[a] += 1
            neighbors[b].append(a)
        
        # Pick the ones with zero incoming edges, we have to visit this first
        q  = deque()
        for i,c in enumerate(incoming):
            if c == 0:
                q.append(i)
        
        count = 0 
        
        # Pick neigbors and reduce the incoming edge count and add it to visit. if all the parents are visited
        while(q):
            item = q.popleft()
            count += 1
            for nxt in neighbors[item]:
                incoming[nxt] -= 1
                if (incoming[nxt] == 0):
                    q.append(nxt)
        return count == numCourses