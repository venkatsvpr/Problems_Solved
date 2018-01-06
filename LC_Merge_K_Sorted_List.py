"""
Merge K Sorted List
https://leetcode.com/problems/merge-k-sorted-lists/description/
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def split(lists,start,end):
            if (start == end):
                return lists[start];
            
            mid = (start+end)/2;
            list1 = split(lists,start,mid);
            list2 = split(lists,mid+1,end);
            return merge(list1, list2)
            
        def merge(l1, l2):
            head = point = ListNode(0)
            while l1 and l2:
                if l1.val <= l2.val:
                    point.next = l1
                    l1 = l1.next
                else:
                    point.next = l2
                    l2 = l2.next
                point = point.next
            
            if not l1:
                point.next=l2
            else:
                point.next=l1
            return head.next
        
        if (0 == len(lists)):
            return []
        if (1 == len(lists)):
            return lists[0]
        return split(lists,0,len(lists)-1)
        
