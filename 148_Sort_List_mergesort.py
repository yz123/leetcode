# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
Sort a linked list in O(n log n) time using constant space complexity.
"""

class Solution(object):
    #mergesort
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head = self.mergesort(head)
        return head
    
    def mergesort(self, head):
        if head != None and head.next !=None:
            slow = head
            fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            second = slow.next
            slow.next = None
            first = head
            #print first.val
            #print second.val
            onelist = self.mergesort(first)
            twolist = self.mergesort(second)
            #print first.val
            #print second.val
            head = self.merge(onelist, twolist)
        return head
    
    def merge(self, first, second):
        dummy = ListNode(None)
        cur = dummy
        while first!=None and second!=None:
            if first.val < second.val:
                cur.next = first
                first = first.next
            else:    
                cur.next = second
                second = second.next
            cur = cur.next
            #cur.next = None
        if first ==None:
            cur.next = second
        if second == None:
            cur.next = first
        return dummy.next
