"""
Push into a prioirty stack.
Pop k times and get the element.
_ Also can be done using a max-heap and pop k times
"""
import queue as Q

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        q = Q.PriorityQueue()
        if not nums:
            return
    
        for num in nums:
            q.put(-num)
        
        for i in range(0,k):
            elem = q.get()
        return (-elem)
