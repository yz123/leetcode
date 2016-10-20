"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        return self.search_row_then_col(matrix, target)
        
        #return self.onearray(matrix, target)
    
    def search_row_then_col(self, matrix, target):
        if not matrix: return False
        
        row, col = len(matrix), len(matrix[0])
        
        #search row
        begin, end = 0, row-1
        max_col = col - 1
        
        cur_row = -1
        while begin <= end:
            middle = begin + (end-begin)/2
            if target < matrix[middle][0]:
                end = middle - 1
            elif target > matrix[middle][col-1]:
                begin = middle + 1
            else:
                cur_row = middle
                break
    
        if cur_row == -1: return False
        
        # do binary serach in the cur_row
        begin, end = 0, col-1
        while begin<=end:
            middle = begin + (end-begin)/2
            if matrix[cur_row][middle] > target:
                end = middle -1
            elif matrix[cur_row][middle] < target:
                begin = middle + 1
            else:
                return True
        
        return False
    
    #index = col * i + j
    #given index, i = index/col; j = index % col
    def onearray(self, matrix, target): 
        if not matrix: return False
        
        row = len(matrix)
        col = len(matrix[0])
        
        start, end = 0, row*col-1
        while start <= end:
            middle = start + (end-start)/2
            num = matrix[middle/col][middle%col]
            if num == target: 
                return True
            elif num < target:
                start = middle + 1
            else:
                end = middle -1 
        return False
