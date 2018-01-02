"""
Min Stack
https://leetcode.com/problems/min-stack/description/
"""
class MinStack:
    stack = []
    min_stack = []
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack =  []
        

    def push(self, x):
        if (x is None):
            return;
        

        if (0 == len(self.stack)):
            self.stack.append(x)
            self.min_stack.append(x)
            return;
        
        self.stack.append(x)
        if (self.min_stack[-1] >= x):
            self.min_stack.append(x)
        return
        """
        :type x: int
        :rtype: void
        """
        

    def pop(self):
        """
        :rtype: void
        """
        if (0 == len(self.stack)):
            return 0
        
        x = self.stack.pop()
        if (0 == len(self.min_stack)):
            print (" minstack zero not possoible")
            return 0
        if (x == self.min_stack[-1]):
            self.min_stack.pop()
            
        return x

    def top(self):

        """
        :rtype: int
        """
        if (0 == len(self.stack)):
            return 0
        return self.stack[-1]

    def getMin(self):

        """
        :rtype: int
        """
        if (0 == len(self.min_stack)):
            return 0
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
