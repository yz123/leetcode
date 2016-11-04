"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""

class Solution(object):
    #dp[0][0] = 1
    #dp[0][j] = dp[0][j-1]
    #dp[i][0] = dp[i-1][0]
    #dp[i][j] = dp[i-1][j]+dp[i][j-1]
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.one_dim_dp(m,n)
        return self.two_dim_dp(m,n)
    
    def two_dim_dp(self, m, n):
        dp = [ [0 for j in xrange(n)]  for i in xrange(m)]
        dp[0][0] = 1
        for i in xrange(1, m):
            dp[i][0] = dp[i-1][0]
        for j in xrange(1, n):
            dp[0][j] = dp[0][j-1]
        for i in xrange(1,m):
            for j in xrange(1, n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
                
        return dp[m-1][n-1]  
        
    def one_dim_dp(self, m, n):
        dp = [ 1 for j in xrange(n) ]
        for i in xrange(1,m):
            for j in xrange(1, n):
                dp[j] = dp[j] + dp[j-1]
        return dp[n-1]
        
