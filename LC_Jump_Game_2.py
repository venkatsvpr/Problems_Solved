"""
45. Jump Game II


Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.

Approach:

"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stepCount = 0
        maxSeen = 0
        end = 0
        for i in range(len(nums)-1):
            maxSeen = max (maxSeen, i+nums[i])
            if  (i  == end):
                end = maxSeen
                stepCount += 1
        return stepCount
