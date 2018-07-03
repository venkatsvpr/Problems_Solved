"""
209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
"""
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        sumarray = [0]
        for num in nums:
            sumarray.append(sumarray[-1]+num)

        Q = []
        minlen = len(nums)+1
        for idx,sum in enumerate(sumarray):
            while (Q) and (sum - sumarray[Q[0]] >= s):
                minlen = min(minlen,idx-Q[0])
                Q.pop(0)
            Q.append(idx)

        if (minlen == len(nums)+1):
            return 0
        return minlen
