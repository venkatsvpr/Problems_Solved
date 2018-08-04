"""
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
Seen this question in a real interview before?


"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = ListNode(0)
        temp.next = head
        p1 = temp
        if (head == None):
            return None
        if (head.next == None):
            return head
        while (p1.next != None):
            p0,p1,p2 = p1,p1.next, p1.next.next
            if (p2 == None):
                break;
            p0.next, p1.next,p2.next  =p2,p2.next,p1
        return temp.next
