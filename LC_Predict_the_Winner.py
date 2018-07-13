"""
486. Predict the Winner

Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Approach:
https://www.youtube.com/watch?v=WxpIHvsu1RI
"""
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if (len(nums) == 1):
            return True
        nums.insert(0,0)
        dp = [[[0,0] for x in range(len(nums))] for x in range(len(nums))]

        for i in range(1,len(nums)):
            dp[i][i] = [nums[i],0]

        i = 1
        j = 1

        Start = []
        for i in range(2,len(nums)):
            Start.append((1,i))

        while (Start):
            (i,j) = Start.pop(0)
            while (i < len(nums)) and (j < len(nums)):
                # for an array from i to j.. we can pick the ith element or jth element
                first = max((nums[i] + dp[i+1][j][1]), (nums[j] + dp[i][j-1][1]))
                # based on what is choosen find the second
                if ((nums[i]+dp[i+1][j][1]) > (nums[j]+dp[i][j-1][1])):
                    second = dp[i+1][j][0]
                else:
                    second = dp[i][j-1][0]
                dp[i][j] = [first,second]
                i += 1
                j += 1

        if (dp[1][len(nums)-1][0] >= dp[1][len(nums)-1][1]):
            return True
        return False
