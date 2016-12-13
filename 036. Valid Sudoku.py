"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.is_val(board)
        return self.solution_1(board)
    
    def is_val(self, board):
        length = len(board)
        row = [ set([]) for i in xrange(length) ]
        col = [ set([]) for i in xrange(length) ]
        block = [ set([]) for i in xrange(length) ]
        
        for i in xrange(length):
            for j in xrange(length):
                num = board[i][j]
                if num == ".":
                    continue
                if num in row[i]:
                    return False
                if num in col[j]:
                    return False
                if num in block[ i/3*3 + j/3  ]:
                    return False
                
                row[i].add(num)
                col[j].add(num)
                block[ i/3*3 + j/3 ].add(num)
        return True

    def solution_1(self, board):
        seen = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c!= '.':
                    seen.append( (c, i))
                    seen.append( (j, c) )
                    seen.append( (i/3, j/3, c) )
                    
        return len((set(seen))) == len(seen) 
    
    """
    def solution_1(self, board):
        seen=[x for i, row in enumerate(board) 
                for j, c in enumerate(row) 
                    if c!='.' 
                        for x in ((c,i),(j,c),(i/3,j/3,c))]
        print len(seen), seen
        print len(set(seen)), set(seen)
        return True
        #return len(seen)==len(set(seen))
    """
