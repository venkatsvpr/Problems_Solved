"""
628. Maximum Product of Three Numbers
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""
class Solution(object):
    """
    Approach:
    Pick the two min elements and two max elements.
    the max is (min1,min2,max3) or (max1,max2,max3)

    """
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min1 = min2 = float('inf')
        max1 = max2 = max3 =float('-inf')
        prod = 1
        if (len(nums) == 3):
            for item in  nums:
                prod *= item
            return prod

        for num in nums:
            if (num > max1):
                if (num > max2):
                    if (num > max3):
                        max1 = max2
                        max2 = max3
                        max3 = num
                    else:
                        max1 = max2
                        max2 = num
                elif (num <= max2):
                    max1 = num
            if (num < min2):
                if (num <min1):
                    min2 = min1
                    min1 = num
                else:
                    min2 = num
        if (min2 == float('inf')):
            min2 = 1
        if (min1 == float('inf')):
            min1 = 1
        if (max1 == float('-inf')):
            max1 = 1
        if (max2 == float('-inf')):
            max2 = 1
        if (max3 == float('-inf')):
            max3 = 1
        #print (min1,min2,max1,max2,max3)
        return max(min1*min2*max3, max1*max2*max3)
mysol = Solution([-4,-3,-2,-1,60])
