"""
82. Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
Apporoach:

A recursive approach seemed intutitve to me. Call the recurisve function for head.

it will skip all the similar nodes.. and call for next node.. keep doing this
head ->A A A B C D D E
call for head... skip all the A and then call for B, then return B + call rec for (C)
keep doing this
"""
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def rec(head):
            # head is None cant do anything return None
            if (head == None):
                return None
            # if head next is none.. return head
            if (head.next == None):
                return head
            # Start from head.. skip all similar nodes
            temp = head
            while (temp and temp.next and temp.val == temp.next.val):
                backup = temp.next
                del(temp)
                temp = backup
            # If the loop breaks at head.. means head next is itself different.
            # return head and call rec for head.next
            if (temp == head):
                head.next = rec (head.next)
                return head
            # if the loop goes over and ends.. return None
            elif (temp == None) or (temp.next == None):
                return None
            # else the loop has consumed all the similar guys.. call for temp.next
            else:
                return rec(temp.next)
        return rec(head)
