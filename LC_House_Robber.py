"""
House Robber
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
        profit.append(nums[0])
        profit.append(max(nums[0],nums[1]))
        for i in range(2,len(nums)):
            profit.append(max(profit[i-1],profit[i-2]+nums[i]))
            
        return  (profit[-1])
