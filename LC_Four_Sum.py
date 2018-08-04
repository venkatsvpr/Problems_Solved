"""
18. 4Sum

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
Approach:
pick two numbers by a loop of O(N^2). pick the next two numbers in O(N)
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        Ans = dict()
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                Expect =dict()
                for k in range(j+1,len(nums)):
                    if nums[k] in Expect:
                        ex = target-nums[i]-nums[j]-nums[k]
                        Ans[(nums[i],nums[j],nums[k],ex)]  = True
                    else:
                        Expect[target - nums[i] - nums[j] - nums[k]] = True
        lt = []
        for key in Ans:
            lt.append(key)
        return lt
