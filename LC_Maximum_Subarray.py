"""
Maximum Subarray
https://leetcode.com/problems/maximum-subarray/description/
"""
class Solution(object):
    def maxSubArray(self, nums):
        if nums is None:
            return 0
        if (len(nums)==1):
            return nums[0]
        # Kadane Algorithm
        sum_till_now = 0;
        sum_max  = 0

        for index,num in enumerate(nums):
            sum_till_now += num
            if (index == 0):
                sum_max = sum_till_now
            elif (sum_max < sum_till_now):
                sum_max = sum_till_now

            if (sum_till_now <0):
                sum_till_now = 0;
        return (sum_max)

        """
        :type nums: List[int];
        :rtype: int
        """
