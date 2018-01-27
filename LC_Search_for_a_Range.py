"""
Start Binary search.
===================
--> if number is on left  binary-search on left 
--> if number is on right binary-search on right
--> At the end only if start/end is found copy the same on to the other variable aswell.
"""
Start  = -1
End = -1
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]   
        """
        global Start
        global End
        def mod_search (start, end, nums, target):
            if (start > end):
                return
            global Start;
            global End;
            mid = (start + end)/2
            if (target == nums[mid]):  
                if (mid+1 >= len(nums)):
                    End = mid
                    mod_search (start, mid-1, nums,target)
                elif ((target != nums[mid+1])):
                    End = mid
                    if (start <= mid-1):
                        mod_search (start,mid-1,nums,target)
                if (mid-1 < 0):
                    Start = mid
                    mod_search (mid+1, end, nums, target)
                elif (target != nums[mid-1]):
                    Start = mid
                    if (mid+1 <= end):
                        mod_search (mid+1,end,nums,target)
                else:
                    mod_search (start, mid-1, nums, target)
                    mod_search (mid+1, end, nums, target)
            elif (target > nums[mid]):
                mod_search (mid+1,end,nums,target)
            elif (target < nums[mid]):
                mod_search (start,mid-1,nums,target)
        
        Start = -1
        End = -1
        if (len(nums)>0):
            mod_search (0,len(nums)-1,nums,target)
            if (End == -1):
                End = Start
            if (Start == -1):
                Start = End
        return [Start,End]
