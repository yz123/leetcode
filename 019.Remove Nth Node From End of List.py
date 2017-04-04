"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head==None or n==0:
            return head
        slow=head
        fast=head
        newhead=ListNode(-1)
        newhead.next=head
        pre=newhead
        step=1
        while step<=n:
            fast=fast.next
            step=step+1
        if fast==None:
            return head.next
        while fast.next!=None:
            pre=pre.next
            slow=slow.next
            fast=fast.next
        if slow.next!=None:
            slow.next=slow.next.next
        else:
            pre.next=None
        return head
