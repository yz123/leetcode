"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        return self.o1_space(n)
        
        #return self.o_n_space(n)
        
    def o1_space(self, n):
        if n ==0: return 0
        if n == 1: return 1
        a0 , a1, a2 = 1, 1, 2
        for i in xrange(2, n+1):
            a2 = a0 + a1
            a0, a1 = a1, a2
        return a2
        
    def o_n_space(self, n):
        if n<=0: return 0
        
        dp = [0] * (n+1)
        dp[0]= 1
        dp[1]= 1
        for i in xrange(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        
        return dp[n]
