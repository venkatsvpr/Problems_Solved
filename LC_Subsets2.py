"""
90. Subsets II
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
Approach:

Sort the input first then taken one by one.
For every number that is is different from previous...
take ever element in answer array append it with this number and finaly add it back to the answer
for number that is same as the previous.. do the above step but only for the part that is added back in the last step
this can kept track by storing the starting position.

"""

class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        Ans = [[]]
        for idx,value in enumerate(nums):
            New_Ans = []
            #print (" idx ",idx," value ",value,New_Ans,Ans)
            end = len(Ans)
            if (idx==0) or  (nums[idx-1] != nums[idx]):
                start = 0
            #print (" going to loop from ",start," to ", end)
            for i in range(start,end):
                st = Ans[i][:]
                st.append(value)
                New_Ans.append(st)
            start = end
            Ans += New_Ans
        return Ans
