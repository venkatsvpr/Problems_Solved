"""
303. Range Sum Query - Immutable

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""
"""
approach:
easy problem
use running sum and find differen between two running sum is the sum of al the numbers between them
"""
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.runningSum = [ 0 ]
        rsum =  0
        for n in nums:
            rsum += n
            self.runningSum.append(rsum)


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.runningSum[j+1] - self.runningSum[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
