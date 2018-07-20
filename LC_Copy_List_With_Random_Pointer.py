"""
138. Copy List with Random Pointer
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

Approach:
1) Traverse through the node.. And have the node as key and new node as the value.
2) again traverse through the node... get the next node from hash and fill the next and random for the new nodes.
"""



# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        d = dict()
        d[None] = None
        m = n = head
        while m:
            d[m] = RandomListNode(m.label)
            m = m.next
        while n:
            d[n].next = d[n.next]
            d[n].random = d[n.random]
            n = n.next
        return d[head]
