"""
House Robber

Logic: 
If there is one house. the profit is robbing the house
If there are two houses the profit is robbing the max of the two houses
If there are 3 houses.. the profit is max(profit robbing 2nd house and , profit robbing 1st house + 3rd house)
profit of robbing n houses.. max(profitof robbing(n-1)and before that , profit of robbing (n)  and n
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
