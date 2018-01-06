"""
Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/description/
"""
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (not nums):
            return 0
        
        n = len(nums)
        
        result = current_min = current_max  = nums[0]
        
        for i in range(1,n):
            temp = current_max
            current_max = max(nums[i], current_max*nums[i], current_min*nums[i])
            current_min = min(nums[i], current_min*nums[i], temp*nums[i])
            result = max(current_max,result)
        return (result)
            
