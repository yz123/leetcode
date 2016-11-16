"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""

"""
idea:
A= [ 1 2 3   transpose   [  1 4 7    swap column  [  7 4 1
     4 5 6   =========>     2 5 8    ===========>    8 5 2
     7 8 9                  3 6 9 ]                  9 6 3 ]
   ]
"""
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        #transpose
        for i in xrange(n):
            for j in xrange(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in xrange(n):
            for j in xrange(n/2):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
