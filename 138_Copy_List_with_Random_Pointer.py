"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        #use a dictionary
        if head is None:
            return None
        map={}
        
        node = head
        while node !=None:
            new = RandomListNode(node.label)
            map[node]=new
            node = node.next
        
        node = head
        while node!=None:
            new = map[node]
            if node.next!=None:
                new.next = map[node.next]
            else:
                new.next =None
            if node.random!=None:
                new.random = map[node.random]
            else:
                node.random =None
            node = node.next
        
        return map[head]
        
        
        """
        if head is None:
            return None
        
        #hash table to mark down original codes
        table = {}
        table[id(None)] = None
        
        #first iteration to copy list without pointers
        itr = head
        while itr is not None:
            #save corresponding node with id()
            table[id(itr)] = RandomListNode(itr.label)
            itr = itr.next
        
        #second iteration to copy two pointers
        itr = head
        while itr is not None:
            node = table[id(itr)]
            node.next = table[id(itr.next)]
            node.random = table[id(itr.random)]
            itr = itr.next
        
        return table[id(head)]
        """
