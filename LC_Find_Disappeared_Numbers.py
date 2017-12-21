# Find Disappeared Numbers
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len (nums)
        for i in range(size):
            if (nums[i]<=size):
                index = abs(nums[i])-1
                nums[index] = (-1 * abs(nums[index]))
                
        
        lt = []
        for i in range(size):
            if (nums[i] >0):
                lt.append(i+1)
        
        return lt
