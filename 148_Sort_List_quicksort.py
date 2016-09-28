"""
Sort a linked list in O(n log n) time using constant space complexity.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    #mergesort
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #head = self.mergesort(head)
        head = self.quicksort(head)
        return head
    
    def quicksort(self, head):
        if head != None and head.next !=None:
            pivot = head
            dummy1=ListNode(None)
            dummy2=ListNode(None)
            head = head.next
            while head!=None:
                cur = head
                head = head.next
                if cur.val<= pivot.val:
                    cur.next = dummy1.next
                    dummy1.next=cur
                else:
                    cur.next = dummy2.next
                    dummy2.next = cur
            #print dummy1.next.val
            #print dummy2.next.val
            onelist=self.quicksort(dummy1.next)
            twolist= self.quicksort(dummy2.next)
            
            if onelist!=None:
                cur = onelist
                while cur.next!=None:
                    cur = cur.next
                cur.next = pivot
                pivot.next =twolist    
                pivot = onelist
            else:
                pivot.next=twolist
            head = pivot
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
