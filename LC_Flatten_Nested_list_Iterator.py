# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
    Ans  = []

    # Recursively make it flat
    def make_flat (self,nlt):
        print (" nlt ",nlt)
        Ans = []
        for item in nlt:
            if (item.isInteger()):
                Ans.append(item.getInteger())
            else:
                Ans += self.make_flat(item.getList())
        return Ans

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.Ans = self.make_flat(nestedList)

    def next(self):
        """
        :rtype: int
        """
        return (self.Ans.pop(0))

    def hasNext(self):
        """
        :rtype: bool
        """
        if (len(self.Ans)):
            return True
        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
