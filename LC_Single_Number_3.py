"""
260. Single Number III


Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

"""

"""
The Approach is kind of different..
We know that x xor x will give us zero.
So if we xor all the numbers... all the pair numbers will cancelout each other..
we will ultimately have a xor b.. where a and b are our answer


now we will have to look for a set bit in the bit mask.
Go through the numbers and divide numbers into two pools based on whether the bit is set or not.
keeping xoring  the numbers in seperate pools ultimately  leading to numbers a and b
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor ^= num
        # check for a set bit.. which means there is a difference between two numbers a and b
        # we are looking for that difference.
        mask = 1
        while (0 == xor&mask):
            mask = mask<<1

        a = 0
        b = 0
        for num in nums:
            # pair of numbers will cancel out. ultimatley we will get a and b
            if (num & mask):
                a ^= num
            else:
                b ^= num
        return [a,b]

            
