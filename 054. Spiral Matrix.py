"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        
        res = []
        
        row_begin, row_end = 0, len(matrix)-1
        col_begin, col_end = 0, len(matrix[0])-1
        
        while row_begin<=row_end and col_begin<=col_end:
            
            #print row_begin, row_end, col_begin, col_end
            
            #move right
            for i in xrange(col_begin, col_end+1):
                res.append(matrix[row_begin][i])
            row_begin += 1
            
            #move down
            for i in xrange(row_begin, row_end+1):
                res.append(matrix[i][col_end])
            col_end -= 1
            
            #move left
            if row_begin <= row_end:
                for i in xrange(col_end, col_begin-1, -1):
                    res.append(matrix[row_end][i])
                row_end -=1
            
            #move up
            if col_begin <= col_end:
                for i in xrange(row_end, row_begin-1, -1):
                    res.append(matrix[i][col_begin])
                col_begin += 1
        return res
