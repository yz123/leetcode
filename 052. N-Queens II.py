"""
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
"""

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.result = 0
        
        #which column has been oppupied
        in_col_dict = {}
        self.search(0, in_col_dict, n)
        return self.result
    
    def search(self, row, in_col_dict, n):
        #print "OK", row, n
        if row == n:
            self.result += 1
        else:
            for col in xrange(n):
                #col in other row
                if col in in_col_dict:
                    continue
                #col in diagnal
                if self.diagnal(in_col_dict, col, row):
                    continue
                in_col_dict[col] = row
                self.search(row+1, in_col_dict, n)
                del in_col_dict[col]
    
    def diagnal(self, in_col_dict, col, row):
        for c in in_col_dict:
            r = in_col_dict[c]
            if c-r == col-row or c+r == col+row:
                return True
        return False
        
        
