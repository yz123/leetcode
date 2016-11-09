"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0: return []
        
        res = [ [ 0  for j in xrange(n)] for i in xrange(n) ]
        
        num = 1
        row_begin, row_end, col_begin, col_end = 0, n-1, 0, n-1
        while row_begin <= row_end and col_begin <= col_end:
            #move right
            for i in xrange(col_begin, col_end+1):
                res[row_begin][i]= num
                num+=1
            row_begin+=1
            
            #move down
            for i in xrange(row_begin, row_end+1):
                res[i][col_end]= num
                num+=1
            col_end-=1
            
            #move left
            if row_begin <= row_end:
                for i in xrange(col_end, col_begin-1, -1):
                    res[row_end][i]=num
                    num+=1
                row_end-=1
            
            #move up
            if col_begin <= col_end:
                for i in xrange(row_end, row_begin-1, -1):
                    res[i][col_begin] = num
                    num+=1
                col_begin+=1
        return res
                
