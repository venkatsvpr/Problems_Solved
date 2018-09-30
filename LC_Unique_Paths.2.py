"""
63. Unique Paths II
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""

"""
Approach:

Straight forward dp.
my value = right value + down value
recursive call for rigth and down points..
memoise the answer.

"""
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        def rec (i, j, dp, obs):
            m = len(obs)
            n = len(obs[0])
            if (i >= m ) or (j >= n):
                return 0
            # the ordering is important.. first we find all the error scenarios and then go to a good scenario
            if (obstacleGrid[i][j] == 1):
                return 0
            if (i == m-1) and (j == n-1):
                return 1
            if ((i,j) in dp):
                return dp[(i,j)]
            # my value equals sum of right and down move.
            dp[(i,j)] =  rec(i+1, j, dp, obs) + rec(i, j+1, dp, obs)
            return dp[(i,j)]
        # find the row  and colum size of the grid
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        if (m == 1 and n == 1):
            if (obstacleGrid[0][0] == 0):
                return 1
            return 0
        # memoisation structure
        dp = dict()
        rec (0, 0, dp, obstacleGrid)
        if (0,0) not in dp:
            return 0
        return dp[(0,0)]
        
