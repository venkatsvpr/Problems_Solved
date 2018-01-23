# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
https://leetcode.com/problems/add-two-numbers-ii/description/
Loop through the elements of the linked list. push it to a stack.
pop it out and read it and store it in a list
"""
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        List_l1  = []
        List_l2  = []
        if ((l1 is None) and (l2 is None)):
            return List_l1
        
        while (l1):
            List_l1.append(l1.val)
            l1 = l1.next

        while (l2):
            List_l2.append(l2.val)
            l2 = l2.next
        
        if (len(List_l1) == 0):
            return List_l2
        
        if (len(List_l2) == 0):
            return List_l1
        carry = 0;
        Answer = []
        while (len(List_l1)>0 and len(List_l2)>0):
            sum = List_l1.pop() + List_l2.pop() + carry
            if (sum >= 10):
                carry = 1
            else:
                carry = 0
            sum = sum % 10
            Answer.insert(0,sum)
        
        while (len(List_l1)>0):
            sum = List_l1.pop() + carry
            if (sum >= 10):
                carry = 1
            else:
                carry = 0
            sum = sum % 10
            Answer.insert(0,sum)
        
        while (len(List_l2)>0):
            sum = List_l2.pop() + carry
            if (sum >= 10):
                carry = 1
            else:
                carry = 0
            sum = sum % 10
            Answer.insert(0,sum)
        
        if (carry == 1):
            Answer.insert(0,1)
        return (Answer)
