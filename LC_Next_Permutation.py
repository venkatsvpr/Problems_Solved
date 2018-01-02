"""
Next Permutation 
https://leetcode.com/problems/next-permutation/description/
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        prev = -1
        num = -1
        bFlag = False

        """
        Go from right to left and find a spot where we [i+1]th spot less than ith spot ( i is to  the right of i+1)
        """
        for index,num in enumerate(nums[::-1]):
            if (prev == -1):
                prev = num
                continue;
            if (prev>num):
                bFlag =True
                break;
            prev=num
        
        if (bFlag == False):
            nums[:]=sorted(nums)
            return
        
        prev_index = len(nums)-1-index
        next_big = -1
        next_big_position = -1

        """
        Find the element that  is just bigger than the num in  nums[prev_index:]
        """
        for i in range(prev_index+1,len(nums)):
            if (i == prev_index+1):
                next_big = nums[i]
                next_big_position = i
            if (nums[i] < next_big and nums[i]>num):
                next_big = nums[i]
                next_big_position = i
      
        """ Swap the numbers """
        nums[next_big_position] = num
        nums[prev_index] = next_big
        
        nums[:] = nums[:len(nums)-index]+sorted(nums[len(nums)-index:])
        
        return
