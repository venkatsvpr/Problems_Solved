"""
494. Target Sum

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1
 

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000

"""
"""
We have to split this into two groups wiht + and - signs and the the difference betwee the groups should be 3
      S1 - S2 = target
Also  S1 + S2 = sum(array)

Adding these two,  2 S1 = target + sum(array) 
S1 = (target + sum(array)) /2 
In this case
S1 = (3 + 5)/2  = 4
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def findSubset(s, idx, d):
            ## If the expected sum is there.. 
            ## we can return 1 indicating to the caller that this is an answer
            if  s == 0:
                # Lets say we have a zero expected sum and zeros..
                if idx < len(nums):
                    d[(s,idx)]  =findSubset(s, idx+1, d) + findSubset(s-nums[idx], idx+1, d)
                    return  d[(s,idx)]
                return 1
            if  idx >= len(nums) or s < 0:
                return 0
            if (s,idx) in d:
                return d[(s, idx)]
            # cannot take this number.. so solve subproblem
            if (nums[idx] > s):
                d[(s,idx)] = findSubset(s, idx+1, d)
            # can take this number. but since the number of ways is the question.. try both taking/not taking
            else:
                d[(s,idx)]  =findSubset(s, idx+1, d) + findSubset(s-nums[idx], idx+1, d)
            return d[(s,idx)]
        if sum(nums) < abs(target):
            return 0
        s = (target + sum(nums))
        if s % 2 != 0:
            return 0
        s = s // 2
        d = dict()
        return findSubset(s, 0, d)
            
            
            