"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

步骤一：通过Linked List Cycle的方式，则快慢指针（快指针一次两步，慢指针一次一步）相遇时，则表示存在环，且相遇点在环上。
步骤二：如果环存在，记：
c表示从head到环起始点的距离；
s表示从环起始点到快慢指针相遇点的距离；
cycle表示环的长度；
distance（pointer）表示指针走过的距离；
性质：
a)快指针走过的距离是慢指针走过距离的二倍
b)快指针和慢指针会相遇，是因为快指针已经套了慢指针一圈（且套第一圈时就会相遇，因为快指针快追上慢指针时，相距要么为1要么为2，为1时，下一次移动后相遇，为2时，在经过两次移动相遇）
于是有：
distance（slow）=c+s， distance（fast）=2（c+s）
性质a和b -> distance（fast）-distanc（slow）=cycle=2(c+s) - (c+s) = c+s
-> c = cycle - s
又由于：环长度为cycle，两指针距离环起点距离为s，在走cycle-s则重新到达起点；且c为从head到环起点的距离，所以从head经过距离c会到达环起点，又c=cycle - s；所以用两个指针，同时从快慢指针的相遇点和head出发，每次移动距离为1，经过cycle - s会在环起点相遇。
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        while fast!=None and fast.next!=None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if fast == None or fast.next == None:
            return None
        else:
            while head!=fast:
                head = head.next
                fast = fast.next
            return fast
