"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3

Example 2:

Input: [3,4,-1,1]
Output: 2

Example 3:

Input: [7,8,9,11,12]
Output: 1

Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)):
            if (nums[i] <0) or (nums[i]>=n):
                nums[i] = 0
        for i in range(len(nums)):
            nums[nums[i]%n] += n
        for i in range(1,len(nums)):
            if (nums[i]/n == 0):
                return i
        return len(nums)
