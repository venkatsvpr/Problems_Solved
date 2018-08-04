"""
210. Course Schedule II

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
Approach:
Check if cycle is there
Do topological sort
If there are numbers that canbe added back. add it

"""



class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Do topological sort
        def rec(item,Visited,Ans,graph):
            if (item in Visited):
                return
            Visited.add(item)
            for child in graph[item]:
                rec(child, Visited,Ans,graph)
            Ans.append(item)
            return

        # check if cycle is there
        def is_cycle(item, graph,Black, Grey, White):
            if (item in Grey):
                return True
            if (item in Black):
                return False
            White.remove(item)
            Grey.add(item)
            for child in graph[item]:
                if (True == is_cycle(child,graph, Black,Grey,White)):
                    return True
            Grey.remove(item)
            Black.add(item)


        White = set()
        Black = set()
        Grey = set()

        Visited = set()
        Ans = []

        graph  = collections.defaultdict(list)
        for [s,pr] in prerequisites:
            graph[pr].append(s)
            White.add(pr)
            White.add(s)

        for key in graph.keys():
            if (key not in White):
                continue
            if (True == is_cycle(key, graph, Black, Grey, White)):
                return Ans


        for key in graph.keys():
            rec(key,Visited,Ans,graph)

        # add courses back which have no dependency
        if (numCourses != len(Ans)):
            for i in range(numCourses):
                # we can even add ans to a set and do O(1) lookup
                if (i not in Ans):
                    Ans.append(i)
        return list(reversed(Ans))
