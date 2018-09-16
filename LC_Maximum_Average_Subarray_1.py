"""
643. Maximum Average Subarray I

Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
"""

"""
push data into a priority queue wiht (idx,data)
have the running sum... store it into runningsum/k
pop elements out of sizek out of the priority queue
"""
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        rsum = 0
        start = 0
        end = 0
        maxavg = float('-inf')
        while (end < len(nums)):
            rsum += nums[end]
            #print (" adding ",nums[end],start,end)
            if (end-start+1) < k:
                end += 1
                continue;
            #print (" rsum ",rsum,start,end)
            maxavg = max (maxavg, rsum/float(k))
            rsum -= nums[start]
            start += 1
            end += 1
        return maxavg
        
