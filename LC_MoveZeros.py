"""
Linearly search the nums and store the position of the zero
Swap the position when we find a non-zero number.
"""
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 
        
        zero_pos  = -1
        index = 0
        while (index <len(nums)): 
            if (nums[index] != 0):
                if (zero_pos != -1):
                    nums[index],nums[zero_pos] = nums[zero_pos],nums[index]
                    index = zero_pos + 1
                    zero_pos = -1
                    continue;                    
                index = index +1
                continue;
            else:
                if (zero_pos != -1):
                    index = index+1
                    continue;
                zero_pos = index
                index = index+1
                continue;
        return
