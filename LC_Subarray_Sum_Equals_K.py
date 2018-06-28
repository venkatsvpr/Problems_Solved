"""
560. Subarray Sum Equals K
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Approach:
        =========
        1) We attempt it by the running sum
        2) at evey element have a dict for the running sum.. if running sum is already present increment the count. else insert with count 1
        3) at every step check if runningsum-k is there on the dict.. if it is there add the number of times it is present to the count.
        """
        running = dict()
        rsum = 0
        running[0] = 1
        count = 0
        for num in nums:
            rsum += num
            if (rsum - k ) in running:
                count += running[rsum-k]
            if (rsum in running):
                running[rsum] += 1
            else:
                running[rsum] = 1
        print (running)
        return count

mysol = Solution()
print (mysol.subarrySum([1,1,1],2))
