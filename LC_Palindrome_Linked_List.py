"""
234. Palindrome Linked List


Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def rec_rev (node):
            if (node == None):
                return None
            elif (node.next == None):
                return node
            else:
                retval = rec_rev(node.next)
                node.next.next =node
                return retval

        def find_mid (node):
            fast = slow = node
            if (node == None):
                return None
            while (fast != None) and (fast.next != None):
                fast = fast.next.next
                if (fast == None):
                    break;
                slow = slow.next
            return slow

        def check_same(first, second):
            #print ("check same ",first.val,second.val)
            while (second != None):
                if (first.val != second.val):
                    #print (first.val,second.val,"returning false")
                    return False
                first = first.next
                second = second.next
            return True

        if (head == None):
            return True

        # Find the middle element
        mid = find_mid(head)

        # Reverse the element from mid
        retval = rec_rev(mid.next)
        if (mid.next != None):
            mid.next.next = None
            mid.next = retval

        # Check the element from first to mid and mid to end.
        retval = check_same(head,mid.next)

        # Reverse the elemnt from mid back to same
        reval = rec_rev(mid.next)
        if (mid.next != None):
            mid.next.next = None
            mid.next =retval

        return retval
