"""
179. Largest Number


Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.

"""


import functools
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # This is the property. See if s1+s2 is bigger than s2+s1
        def cmp (s1,s2):
            if (s1 == s2):
                return 0
            if (s1+s2) > (s2+s1):
                return -1
            else:
                return 1

        Nums = [str(num) for num in nums]
        Nums = sorted(Nums, key =functools.cmp_to_key(cmp))
        if (Nums[0] == "0"):
            return "0"

        St = ""
        for num in Nums:
            St+=num
        return St
