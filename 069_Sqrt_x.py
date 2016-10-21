"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return self.binary_search(x)
        
        return self.bit_operation(x)
    
    #https://discuss.leetcode.com/topic/2671/share-my-o-log-n-solution-using-bit-manipulation/12 
    #As x is int, the maximum of x is 2^31-1, sqrt(x)'s most significant bit is at most 2^15. But (2^15 + 2^14)^2 exceeds int, not unsigned int, so I use unsigned int to represent sqrt(x) as res, so res * res will never overflow. Here is my code
    def bit_operation(self,x):
        res = 0
        for i in xrange(15, -1, -1):
            tmp = res + (1<<i)
            if tmp*tmp <=x:
                res += (1<<i)
        return res
    
    #https://discuss.leetcode.com/topic/63978/c-binary-search-3-ms    
    def binary_search(self,x):
        if x == 0 or x==1: return x
        
        l, r = 0, min( (x>>1)+1, 46341)
        while l<r-1:
            m = (l + r) >> 1
            if m*m>x:
                r = m
            else:
                l = m
        return l
            
