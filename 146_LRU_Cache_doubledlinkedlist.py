"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
"""


class list(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None
        
#https://discuss.leetcode.com/topic/58662/python-map-and-double-linked-list
#head is the least recently used
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.head = list(None, None)
        self.tail = self.head
        self.map = {}

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.map:
            node = self.map[key]
            value = node.value
            
            #move node to the tail
            self.move_to_tail(node)
            
            
            return value
            
        return -1
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.move_to_tail(node)
        else:
            node = list(key, value)
            #add to the tail
            node.pre = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node
            self.map[key]=node
            
            if self.head.key == None:
                self.head = node
                
            if self.cap > 0:
                self.cap -= 1
            else:
                #move the first one
                delkey = self.head.key
                if self.head.next!=None:
                    self.head.next.pre = None
                self.head = self.head.next
                self.map.pop(delkey)

            
    def move_to_tail(self, node):
        #node is at the beginning
        if node.pre ==None:
            if self.head.next !=None:
                self.head = self.head.next
                self.tail.next = node
                node.pre = self.tail
                self.tail = node
                node.next = None
        #node is in the middle
        elif node.next !=None:
            nb = node.pre
            nn = node.next
            nb.next = nn
            nn.pre = nb
            self.tail.next = node
            node.pre = self.tail
            self.tail = node
            node.next = None
