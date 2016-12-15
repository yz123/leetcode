"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        #solution 1: log based solution: change to substract
        
        #solution 2:
        #https://discuss.leetcode.com/topic/8714/clear-python-code/2
        #https://discuss.leetcode.com/topic/15568/detailed-explained-8ms-c-solution/2
        
        positive =  ( (dividend < 0) == (divisor < 0 ) )
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp = divisor
            i = 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i = i<< 1
                temp = temp << 1
        if not positive:
            res = -res
        #return  res
        return min(res, 2147483647)
        
 
    
    #return min(max(-2147483648, res), 2147483647)
