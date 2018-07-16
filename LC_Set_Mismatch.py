"""
645. Set Mismatch

The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.
"""

"""
Find the duplicate by marking the numbers by  *-1
The index that is left with a positive value after this process is the missing number.
"""
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        duplicate = 0
        missing = 0
        for i in range(len(nums)):
            if (nums[abs(nums[i])-1] < 0):
                duplicate = abs(nums[i])
                continue;
            nums[abs(nums[i])-1] *= -1

        for i in range(len(nums)):
            if (nums[i] > 0):
                missing = i+1
        return [duplicate, missing]
