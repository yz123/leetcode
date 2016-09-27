"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head!=None and head.next!=None:
            slow = head
            fast = head
            while fast.next != None and fast.next.next!= None:
                fast = fast.next.next
                slow = slow.next
            
            half = slow.next
            slow.next =None
                
            #逆转后面的一半
            dummy = ListNode(-1)
            while half!=None:
                temp = half
                half = half.next
                temp.next = dummy.next
                dummy.next = temp
                
            # insert
            
            half = dummy.next
            #print half.val
            head1 = head
            while half!=None:
                #print head1.val
                #print half.val
                temp = half.next
                half.next = head1.next
                head1.next = half
                head1 = head1.next.next
                half=temp
