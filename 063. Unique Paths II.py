"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
"""

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        g = obstacleGrid
        if not g: return 0
        
        m, n = len(g), len(g[0])
        
        for i in xrange(m):
            for j in xrange(n):
                if i==0 and j==0:
                    g[i][j] = ( 1 if g[i][j]==0 else 0 )
                elif i==0:
                    g[0][j] = ( g[0][j-1] if g[0][j]==0 else 0 )
                elif j==0:
                    g[i][0] = ( g[i-1][0] if g[i][0]==0 else 0 )
                else:
                    g[i][j] = ( ( g[i-1][j] + g[i][j-1]) if g[i][j]==0 else 0 )
                    
        return g[m-1][n-1]
