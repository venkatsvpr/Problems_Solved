"""
148. Sort List


Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
Approach:
=========
divide and conquer.
keep slow and fast pointer and divide the list into two parts.
keep doing it recurisvely and merge it.

"""
class Solution(object):
    def sortList (self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (not head) or (not head.next):
            return head;
        # Keep slow and fast pointer, divide the list into two
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        # Split int two lists
        left = self.sortList(head)
        right = self.sortList(second)
        # Merge the two lists into one.
        return self.merge(left, right)

    # Merging two sorted list
    def merge (self, left, right):
        if not left or not right:
            return left or right
        if left.val > right.val:
            left, right = right, left
        # Start  tempNode and merge nodes
        tempNode = ListNode(0)
        start = tempNode
        while (left and right):
            if (left.val < right.val):
                tempNode.next = left
                tempNode = tempNode.next
                left = left.next
            else:
                tempNode.next = right
                tempNode = tempNode.next
                right = right.next
        tempNode.next = left or right
        return start.next
