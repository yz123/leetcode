# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l=ListNode(0)
        head = l
        while l1!=None or l2!=None:
            if l1!=None:
                l.val += l1.val
                l1=l1.next
            if l2!=None:
                l.val += l2.val
                l2=l2.next
                
            flag = l.val/10
            if l1!=None or l2!=None or flag!=0:
                l.next =ListNode(l.val/10)
                l.val %= 10
                l=l.next
        
        return head
