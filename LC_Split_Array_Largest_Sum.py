"""
410. Split Array Largest Sum

Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

 

Example 1:

Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], m = 2
Output: 9
Example 3:

Input: nums = [1,4,4], m = 3
Output: 4
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 106
1 <= m <= min(50, nums.length)
"""

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # Is valid check if we can create m continous subarray with sum of max s
        def isValid(s):
            rSum = 0
            groups = 1
            for i in nums:
                rSum += i
                if rSum > s:
                    rSum = i
                    groups += 1
                if groups > m:
                    return False
            return True
        
        # The least sum would max of all the elements
        start = max(nums)
        # the max sum would be sum of all the elements
        end = sum(nums)
        res = -1
        
        # search the problem space
        while (start <= end):
            mid = start + (end -start)//2
            if isValid(mid):
                res = mid
                end = mid -1 
            else:
                start = mid + 1
        
        # return the result
        return res