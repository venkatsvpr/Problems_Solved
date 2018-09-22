"""
92. Reverse Linked List II


Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
Approach:
have a function to reverse from a node to a count n
start from head and navigate m nodes... decrmeent n for every time.
Return the new head and the next element(n2)

call this for head.next.
connect head.next.next as the next element(n2)
connect head.next= newhead

"""
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        def rev (node, count):
            if (count == 1):
                return node, node.next
            retval = rev(node.next, count-1)
            node.next.next = node
            return retval

        m -= 1
        n -= 1
        start = head
        # find the start point
        while (m > 1):
            start = start.next
            m -= 1
            n -= 1
        # return the head if  one element to reverse
        if (n < 1):
            return head
        # use this and map the pointers
        retval = rev(start.next, n)
        if (m == 0):
            head.next.next =head;
            head.next = retval[1]
            return retval[0]
        start.next.next = retval[1]
        start.next =retval[0]
        return head
        
