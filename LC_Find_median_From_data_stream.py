"""
295. Find Median from Data Stream

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
 

Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

"""
import queue
class MedianFinder:
    def __init__(self):
        self.left = queue.PriorityQueue()
        self.right = queue.PriorityQueue()

    def addNum(self, num: int) -> None:
        if self.left.qsize() == 0:
            self.left.put(-num)
            return
        
        leftMax = -1 *self.left.get()
        self.left.put(-1 * leftMax)
        
        if num < leftMax:
            self.left.put(-1 * num)
        else:
            self.right.put(num)
        
        if (self.right.qsize() - self.left.qsize()) == 2:
            self.left.put(-1 * self.right.get())
        elif (self.left.qsize() - self.right.qsize()) == 2:
            self.right.put(-1 * self.left.get())
        return
    def findMedian(self) -> float:
        if self.left.qsize() > 0:
            leftMax = -1 *self.left.get()
            self.left.put(-1 * leftMax)
        
        if self.right.qsize() > 0:
            rightMin = self.right.get()
            self.right.put(rightMin)
        
        if self.left.qsize() == self.right.qsize():
            return (leftMax + rightMin)/2.0
        if self.left.qsize() > self.right.qsize():
            return leftMax
        return rightMin
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

import queue
class MedianFinder:
    def __init__(self):
        self.left = queue.PriorityQueue()
        self.right = queue.PriorityQueue()

    def addNum(self, num: int) -> None:
        self.right.put(num)
        
        fromRight = self.right.get()
        self.left.put(-1 * fromRight)
        
        if self.right.qsize() < self.left.qsize():
            fromLeft = self.left.get()
            self.right.put(-1 * fromLeft)
        return
    
    def findMedian(self) -> float:
        if self.left.qsize() > 0:
            leftMax = -1 *self.left.get()
            self.left.put(-1 * leftMax)
        
        if self.right.qsize() > 0:
            rightMin = self.right.get()
            self.right.put(rightMin)
        
        if self.left.qsize() == self.right.qsize():
            return (leftMax + rightMin)/2.0
        return rightMin