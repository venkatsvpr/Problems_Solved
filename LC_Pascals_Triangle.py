"""
118. Pascal's Triangle
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
"""
Approach:
Take [1] for a level first..
keep building a new level and go on and on
return when we reach the result level
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def getNext (Lt):
            tAns = []
            for i in range(len(Lt)-1):
                tAns.append(Lt[i]+Lt[i+1])
            return tAns
        if (numRows == 0):
            return []
        Ans = [[1]]
        for i in range(numRows-1):
            if (1 == len(Ans[-1])):
                Ans.append([Ans[0][0], Ans[-1][0]])
            else:
                Ans.append([Ans[0][0]] + getNext(Ans[-1]) + [Ans[-1][0]])
        return Ans
