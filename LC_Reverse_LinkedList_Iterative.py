# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
Iteratively use 3 pointers. Swap them lineraly
"""
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None):
            return None
        
        if (head.next == None):
            return head
        
        curr = head;
        p = head.next;
        head.next = None;
        q = None;
        while (p):
            q = p.next
            p.next = curr;
            curr = p;
            p = q;
        
        return (curr)
