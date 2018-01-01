"""
Remove Element
https://leetcode.com/problems/remove-element/
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
                
        while (val in nums):
            index = nums.index(val)
            del nums[index]

        return len(nums)            
