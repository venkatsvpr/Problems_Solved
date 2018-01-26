"""
https://leetcode.com/problems/lru-cache/description/
Have a dict to fetch the value from key at O(1)
Have a DLL. when we put or get update at the end. when the lenght is  more delete the first
"""
class myNode:
    def __init__ (self,key,val):
        self.val = val;
        self.key = key;
        self.next = None;
        self.prev = None;
    
class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = dict()
        self.head = myNode(0,0)
        self.tail = myNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def delete1 (self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        
    def add1 (self, node):
        prev = self.tail.prev
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail
        prev.next = node
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            node = self.dict[key]
            self.delete1(node)
            self.add1(node)
            return node.val
        return -1
    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = myNode(key,value)              
        if key in self.dict:
            self.delete1(self.dict[key])
        self.add1(node)
        self.dict[key] = node

        if (len(self.dict)>self.capacity):
            node = self.head.next
            self.delete1(node)
            del (self.dict[node.key])    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
