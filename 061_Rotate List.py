"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        """
        Given 1->2->3->4->5->NULL and k = 2,
        return 4->5->1->2->3->NULL.
        """
        
        if not head or not head.next: return head
        
        #count the length of list
        tail, length = head, 1
        while tail.next:
            tail = tail.next
            length += 1
        
        #make it circle
        tail.next = head
        
        k = k%length
        for i in xrange(length-k):
            tail = tail.next
        
        head = tail.next
        tail.next = None
        return head
        
