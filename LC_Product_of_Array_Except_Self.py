"""
Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/description/
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    # Perform multiplication of elements from left and right seperately. then mulitply both
    # [ 1 2 3 4]
    # After left multiplication  [ 1 1 2 6]
    # After right multiplication [ 24 12  4 1]
    # Multiply these two         [24 12 8 6] - This is the answer.
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        new_output = []
        
        p = 1
        for i in range(0,n):
            new_output.insert(0,p)  
            p = p * nums[n-1-i]
           
        for i in range(0,n):
            output[i] = output[i] * new_output[i]
        
        return (output)

