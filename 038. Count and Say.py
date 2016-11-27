"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n ==0: return "1"
        
        num = "1"
        for _ in xrange(1, n):
            num = self.get_next(num)
            
        return num
    
    def get_next(self, num):
        next = ""
        i, j = 0, 0
        while j<len(num):
            if num[j]!=num[i]:
                next+=str(j-i)+num[i]
                i = j
            j+=1
        #last charactor
        next+=str(j-i)+num[i]
        return next
