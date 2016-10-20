"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

#idea: use the first row and left col to store whether needs to be 0. 
#if there is a 0 in (i,j), set matrix[i][0]=0, matrix[0][j]=0 

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix: return
        
        #check if the first row or left column needs to be 0
        first_row, left_col = False, False
        
        row, col = len(matrix), len(matrix[0])
        for i in xrange(row):
            for j in xrange(col):
                if matrix[i][j] ==0:
                    if i == 0:
                        first_row = True
                    if j == 0:
                        left_col = True
                    
                    if i>0 and j>0:
                        matrix[0][j] =0
                        matrix[i][0] = 0
        
        #set row to be zeros
        for i in xrange(1, row):
            if matrix[i][0]==0:
                for j in xrange(1, col):
                    matrix[i][j] = 0
        
        #set col to be zeros
        for j in xrange(1, col):
            if matrix[0][j] ==0:
                for i in xrange(1, row):
                    matrix[i][j] = 0
        
        #set first row and left col to be 0s
        if first_row:
            for j in xrange(col):
                matrix[0][j] = 0
        if left_col:
            for i in xrange(row):
                matrix[i][0] = 0
        
