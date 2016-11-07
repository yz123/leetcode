"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.result = []
        
        is_in_dict = {}
        self.search(0, is_in_dict, n)
        return self.result
    
    def search(self, row, is_in_dict, n):
        if row == n:
        #print the result
            sol = [""]*n
            for c in xrange(n):
                tmp = ["."]*n
                r = is_in_dict[c]
                tmp[c] = "Q"
                sol[r]= "".join(tmp)
            #for c, r in is_in_dict.items():
            #for c, r in is_in_dict.iteritems():
            #    sol[r][c] = "Q"
            self.result.append(sol)
        else:
            for col in xrange(n):
                if col in is_in_dict:
                    continue
                if self.is_diagnal(row, col, is_in_dict):
                    continue
                is_in_dict[col]=row
                self.search(row+1, is_in_dict,n)
                del is_in_dict[col]
    
    def is_diagnal(self, row, col, is_in_dict):
        for c in is_in_dict:
            r = is_in_dict[c]
            if c-r == col-row or c+r == col+row:
                return True
        return False
        
