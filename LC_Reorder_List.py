"""
143. Reorder List


Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
find the middle element..
From middle to end reverse.
point.. slow to mid.. mid to slow.next and keep doing it

"""
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # Reverse from a node
        def reverse (node):
            if (node.next == None):
                return node
            retval = reverse(node.next)
            node.next.next = node
            return retval

        if (head == None):
            return None
        if (head.next == None):
            return
        if (head.next.next == None):
            return

        # Use slow fast pointer to find the middle
        slow = head
        fast = head
        prev = None
        while (slow == head) or ((fast != None) and (fast.next != None)):
            slow = slow.next
            fast = fast.next.next
            prev = slow

        # Try to reverse
        newhead = reverse(prev.next)
        prev.next.next = None
        prev.next = None
        fast = newhead
        slow = head

        while (fast and slow):
            # Take a backup of the fast and slow next
            fastnext = fast.next
            slownext = slow.next
            # make the pointers loop
            slow.next = fast
            fast.next = slownext
            # when it reaches the end
            if (fast.next == None):
                fast.next = fastnext
                break;
            # move the slow and fast to next
            slow = slownext
            fast = fastnext
