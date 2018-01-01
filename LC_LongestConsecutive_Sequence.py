"""
Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/description/
"""
class Solution:
    def longestConsecutive(self, nums):
        
        """
        :type nums: List[int]
        :rtype: int
        """ 
        
        """ Add the numbers to dictionary  """
        d = dict()
        for num in nums:
            d[num] = 1
        
        max_count = 0
        
        """ For all keys in dictionary """
        for key in d:
            count = 1
            """ 
            If the key-1 is in dictionary.
            If 4,2,3,1,0 are in the dict. we continue for 4,2,3,1 and when we hit the  0 case.
            we could 1,2,3,4
            """
            if (key-1 in d):
                continue

            if (key+1 in d):
                cont =  True;
                while(cont):
                    if (key+1 in d):
                        count += 1
                    else:
                        cont = False;
                    key = key+1
            """ 
            Keep a track of max_count
            """
            if (count >max_count):
                max_count =count
 
        return (max_count)
