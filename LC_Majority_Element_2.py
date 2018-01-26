"""
https://leetcode.com/problems/majority-element-ii/description/
First find the two most significant element
Find the number of times the number occurs in the array.
If the two most significant numbers exist for more than len/3 store it in a list and return the answer.
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        a,b,count_a,count_b = 0,-1,0,0
        for num in nums:
            if (num == a):
                count_a += 1
            elif (num == b):
                count_b += 1
            elif (count_a == 0):
                a,count_a = num,1
            elif (count_b == 0):
                b,count_b = num,1
            else:
                count_a = count_a - 1
                count_b = count_b - 1
        Answer = []
        count_a = len( [0 for num in nums if num==a ])
        if (count_a > len(nums)/3):
            Answer.append(a)
            
        if (a==b):
            return Answer
        
        count_b = len( [0 for num in nums if num==b])
        if (count_b > len(nums)/3):
            Answer.append(b)
        return Answer
        
        
        
            
