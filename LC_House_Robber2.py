"""
House Robber
https://leetcode.com/problems/house-robber/description/
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        if (len(nums)== 1):
            return nums[0]
        profit = []
        a = nums [0]
        b = max (nums[0],nums[1])
        c = b
        for i in range(2,len(nums)):
            c = max(a+nums[i],b)
            a,b = b,c
            
        return  (c)
