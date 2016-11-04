"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return self.inplace(grid)
        return self.dp(grid)
    
    # g[0][j] = g[0][j-1] + g[0][j]
    # g[i][0] = g[i-1][0] + g[i][0]
    # g[i][j] = min( g[i-1][j], g[i][j-1] ) + g[i][j]
    def inplace(self, grid):
        m, n = len(grid), len(grid[0])
        g = grid
        
        for i in xrange(1, m):
            g[i][0] = g[i-1][0] + g[i][0]
        
        for j in xrange(1, n):
            g[0][j] = g[0][j-1] + g[0][j]
        
        for i in xrange(1, m):
            for j in xrange(1, n):
                g[i][j] = min( g[i-1][j], g[i][j-1] ) + g[i][j]
        return g[m-1][n-1]
    
    # dp[0][0] = grid[0][0]
    # dp[0][j] = dp[0][j-1] + grid[0][j]
    # dp[i][0] = dp[i-1][0] + grid[i][0]
    # dp[i][j] = min( dp[i-1][j], dp[i][j-1] ) + grid[i][j]
    def dp(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [  [ 0 for j in xrange(n) ]   for i in xrange(m) ]
        
        dp[0][0] = grid[0][0]
        for i in xrange(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
            
        for j in xrange(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[i][j] = min( dp[i-1][j], dp[i][j-1] ) + grid[i][j]
        return dp[m-1][n-1]
