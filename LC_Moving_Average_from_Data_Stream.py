"""
Moving Average from Data Stream
https://leetcode.com/problems/moving-average-from-data-stream/

Approach:
1) Create a Queue for the size
2) Enqueue and dequeue
3) Keep track of the sum of elements queue
4) When we pop - we have to update the sum and return 
"""
class MovingAverage:
    queue_sum = 0;
    queue = [];
    maxsize = 0;
    
    def __init__(self, size):
        
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue_sum = 0;
        self.queue = list()
        self.maxsize = size
        return
    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if (self.maxsize == len(self.queue)):
            out_val = self.queue.pop()
            self.queue_sum -= out_val
            self.queue_sum += val
            self.queue.insert(0,val)
        else:
            self.queue_sum += val
            self.queue.insert(0,val)
        return (self.queue_sum/len(self.queue))
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
