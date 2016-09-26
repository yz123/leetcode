"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
"""

"""
class LRUCache(object):

    def __init__(self, capacity):
       
        self.cap = capacity
        self.num = 0
        self.least_index = None
        self.ele = {}
        self.used_count = {}
        

    def get(self, key):
       
        if key not in self.ele:
            return -1
        else:
            old_count = self.used_count[key]
            self.used_count[key] += 1
            if self.least_index == key: 
                self.least_index = min(self.used_count.items(), key=lambda x: x[1])[0]
                
            return self.ele[key]
        

    def set(self, key, value):
        
        if key in self.ele:
            self.ele[key]=value
            #self.used_count[key]+=1
            #if self.least_index == key:
            #    self.least_index = min(self.used_count.items(), key=lambda x: x[1])[0]
        else:
            if self.num < self.cap:
                self.num +=1
                
                self.used_count[key]=1
                self.ele[key]=value
                if self.least_index == None:
                    self.least_index = key
            
            else:
                #del self.ele[self.least_index]
                #del self.used_count[self.least_index]
                self.ele.pop(self.least_index)
                self.used_count.pop(self.least_index)
                
                
                
                
                #add key
                self.ele[key]=value
                self.used_count[key]=1
                
                #find least used
                self.least_index = min(self.used_count.items(), key=lambda x: x[1])[0]
"""

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = collections.OrderedDict()
        self.remain = capacity
        

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.dic:
            value = self.dic.pop(key)
            self.dic[key]=value
            return value
        return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                #The pairs are returned in LIFO order if last is true or FIFO order if false.
                self.dic.popitem(last=False) 
            
        self.dic[key]=value
