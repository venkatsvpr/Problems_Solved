"""
416. Partition Equal Subset Sum
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def hasSubset (s):
            n = len(nums)
            dp = [[False for j in range(s+1)] for i in range(n+1)]
            for i in range(n+1):
                for j in range(s+1):
                    if j == 0:
                        dp[i][j] = True
            
            for i in range (1,n+1):
                for j in range(1,s+1):
                    # If the number is big we cannot do anything, so check the same sum without the number
                    if nums[i-1] > j:
                        dp[i][j] = dp[i-1][j]
                    else:
                        # we have two decisions, pick it or not pick it
                        # if we pick, the check the best value for newSum = j - nums[i] in the nums without the current number
                        dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
            return dp[len(nums)][s]
        
        # To do this the sum should be even
        if sum(nums) % 2 != 0 :
            return False
        
        return hasSubset(sum(nums)/2)



class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        t = dict()
        def canDoSubset(nums, req):
            # base conditions
            if req == 0:
                return True
            if len(nums) == 0:
                return False            
            
            if (len(nums), req) in t:
                return t[(len(nums), req)]
            
            # If the number if soo big, cant include them
            if (nums[0] > req):
                t[(len(nums), req)] = canDoSubset(nums[1:], req)
                return t[(len(nums), req)]
            
            # Take best of taking the first number or not taking.
            t[(len(nums), req)] = canDoSubset(nums[1:], req-nums[0]) or canDoSubset(nums[1:], req)        
            
            return t[(len(nums), req)]
        reqSubsetSum = sum(nums)
        
        # can be partiotioned only if it is even
        if reqSubsetSum % 2 != 0:
            return False
        
        # We want a subset, The rest would be another equal subset
        reqSubsetSum = int(reqSubsetSum / 2)
        return canDoSubset(nums, reqSubsetSum)
            
        