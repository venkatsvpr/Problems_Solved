"""
300. Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 0):
            return 0
        dp = [0 for i in range(len(nums))]
        dp[0] = 1
        for i in range(1,len(nums)):
            maxIter = 0
            for j in range(i):
                if (nums[j] < nums[i]):
                    maxIter = max (maxIter, dp[j])
            dp[i] = maxIter + 1
        return max(dp)


# Keep a stack of increasing number of items
# if we get a new number which is big.. add ot hte stack
# If the number is small or equal. find the position in the stack and swap it out.
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = 0
        if len(nums) == 0:
            return ans
        stack = [ nums[0] ]
        ans = 1
        for idx in range(1,len(nums)):
            if stack[-1] < nums[idx]:
                stack.append(nums[idx])
            else:
                idx2 = 0 
                ## do binary search here
                while idx2 < len(stack) and stack[idx2] < nums[idx]:
                    idx2 += 1
                stack[idx2] = nums[idx]
            ans = max(ans,len(stack))
        return ans
                
            
            
            