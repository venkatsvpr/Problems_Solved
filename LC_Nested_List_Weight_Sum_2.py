"""
364. Nested List Weight Sum II

Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

Example 1:

Input: [[1,1],2,[1,1]]
Output: 8
Explanation: Four 1's at depth 1, one 2 at depth 2.
Example 2:

Input: [1,[4,[6]]]
Output: 17
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17.

"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

"""
Approach:
Similar to the previous problem.
1) use a traversal.. note the depths and the elements seen on the depth..
also keep track of max value.
Since we are doing it the reverse way... the value would be the
(maxdepth - percieved depth + 1) multiplied by the item seen.

keep track fo the sum and return the sum
"""
class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if (len(nestedList) == 0):
            return 0
        queue = []
        sum = 0
        for n in nestedList:
            queue.append((n,1))

        Ans  = collections.defaultdict(list)
        maxdepth = 1
        while (queue):
            next,depth = queue.pop(0)
            if (next.isInteger()):
                Ans[depth].append(next.getInteger())
                maxdepth = max(depth,maxdepth)
            else:
                for i in next.getList():
                    queue.append((i, depth+1))
        for key in Ans.keys():
            for item in Ans[key]:
                sum += (maxdepth-key+1)*item
        return sum
