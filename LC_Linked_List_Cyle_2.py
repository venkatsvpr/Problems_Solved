"""
142. Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
"""

"""
Hav a fast and slow pointer.. move slow pointer by 1 hop .. move fast pointer by 2 hops.
find the point where they meet. store that point.

now start two pointers one from start and other from that point and incremeent both by single step.
they will meet at somepoint
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None) or (head.next == None):
            return None

        slow = fast = head;
        while (True):
            if (fast == None) or (fast.next == None) or (fast.next.next == None):
                return None
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                break;
        pt1 = head
        pt2 = fast
        while ((pt1 != pt2) and (pt1 != None) and (pt2 != None)):
            pt1 = pt1.next
            pt2 = pt2.next

        return pt1  
