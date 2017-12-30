# Summary Ranges
# https://leetcode.com/problems/summary-ranges/description/
class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        prev = start = 0;

        Ans = list()
        
        # Go linearly in the array... Keep track of the start and the prev number. 
        # check if the current number is next to prev ie. curren-prev =1. 
        # When this condition is violated. push the "start->end" into a list.
        # At the end if start/end is there  push it to the list.
        # Return the list
        for index,item in enumerate(nums):
            if (index == 0):
                prev = item
                start = item
                continue;
                
            if (item - prev == 1):
                prev = item
                continue;
            else:
                if (start != prev):
                    Ans.append(str(start)+"->"+str(prev))
                else:
                    Ans.append(str(start))
                start = item
                prev = item
        
        if (start != prev):
            Ans.append(str(start)+"->"+str(prev));
        else:
            Ans.append(str(start))
                
        return (Ans)
