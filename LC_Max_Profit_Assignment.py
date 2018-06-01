"""
826. Most Profit Assigning Work
=================================
We have jobs: difficulty[i] is the difficulty of the ith job, and profit[i] is the profit of the ith job.

Now we have some workers. worker[i] is the ability of the ith worker, which means that this worker can only complete a job with difficulty at most worker[i].

Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.  If a worker cannot complete any job, his profit is $0.

What is the most profit we can make?

Example 1:

Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get profit of [20,20,30,30] seperately.

Notes:

    1 <= difficulty.length = profit.length <= 10000
    1 <= worker.length <= 10000
    difficulty[i], profit[i], worker[i]  are in range [1, 10^5]
"""

class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        # Sort the input based on difficulty and store it in dp
        dp = sorted(zip(difficulty,profit))
        Ans =  i = best = 0
        # Sort the workers based on skill and loop.
        for level in sorted(worker):
            # best variable is the best till the level, When we go higher level we dont have to recmpute from start.
            # We just have to recompute the old level to the new level.
            while (i<len(dp) and level >= dp[i][0]):
                best = max(best, dp[i][1])
                i += 1
            Ans += best
        return Ans

df = [2,4,6,8,10]
pf = [10,20,30,40,50]
wr = [4,5,6,7]

mysol = Solution()
print (mysol.maxProfitAssignment(df,pf,wr))
