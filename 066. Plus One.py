"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #return self.lamda(digits)
        #return self.p_one(digits)
        return self.recursion(digits, len(digits)-1)
    
    def lamda(self, digits):
        num = reduce( lambda x,y: 10*x + y, digits) + 1
        return map( lambda x:int(x), str(num))
    
    def p_one(self, digits):
        for i in xrange(len(digits)-1, -1, -1):
            digits[i] = digits[i]+1
            if digits[i] < 10:
                return digits
            digits[i] = 0
        
        
        digits.insert(0, 1)
        return digits
    
    def recursion(self, digits, index):
        if index < 0: 
            digits.insert(0, 1)
            return digits
        digits[index] = digits[index]+1
        if digits[index] < 10:
            return digits
        else:
            digits[index] = 0
            self.recursion(digits, index-1)
        return digits
