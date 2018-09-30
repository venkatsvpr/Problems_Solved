"""
325. Maximum Size Subarray Sum Equals k

Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
Follow Up:
Can you do it in O(n) time?
"""
"""
Have an hasmap with running sum as key and the index where the running sum was seen as value.
hashmap[runningsum] = index

calculate running sum.. if the same is not in hasmap insert it inot thehasmap with the index.
also.. check.. if runningsum -k is there..if there.. the index - hmap[rsum-k] is greater than maxvalue
update the maxvalue.

"""
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        rsumIndexMap = dict()
        rsumIndexMap[0] = - 1
        rsum = 0
        maxval = float('-inf')

        for idx,num in enumerate(nums):
            rsum += num
            # If rsum is not in hamp.. insert it into the hmap
            if (rsum not in rsumIndexMap):
                rsumIndexMap[rsum] = idx
            # If rsum-k is there... idx - hmap[rsum-k]..
            # if value is bigger than max value update it
            if (rsum-k in rsumIndexMap):
                maxval = max(maxval, idx - rsumIndexMap[rsum-k])
        if (maxval == float('-inf')):
            return 0
        return maxval
