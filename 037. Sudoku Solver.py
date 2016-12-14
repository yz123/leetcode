"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.


A sudoku puzzle...


...and its solution numbers marked in red.
"""

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.backtracking(board)

    def backtracking(self, board):
        length = len(board)

        row = [set([]) for i in xrange(length)]
        col = [set([]) for i in xrange(length)]
        block = [set([]) for i in xrange(length)]
        # check each row to see if it is valid
        # if it is valid, add number to it; else go to other number


        is_valid = self.initilize(board, row, col, block)

        if not is_valid:
            return False


        index = 0
        if self.filling_up(board, index, row, col, block):
            return True
        else:
            return False

    # fill up the current position, and fine the next position to fill
    def filling_up(self, board, index, row, col, block):
        if index > len(board) * len(board)-1:
            return True

        i, j = index / len(board), index % len(board)

        c = board[i][j]


        if c != ".":
            return self.filling_up(board, index + 1, row, col, block)

        #print len(board) * len(board), index, i, j, c

        candidate = "123456789"

        for c in candidate:  # "123456789"
            #print len(board) * len(board), index, i, j, c
            if c in row[i]:
                continue
            if c in col[j]:
                continue
            if c in block[i / 3 * 3 + j / 3]:
                continue

            # add c into the board
            #print c, type(c)
            board[i][j] = c
            row[i].add(c)
            col[j].add(c)
            block[i / 3 * 3 + j / 3].add(c)

            if self.filling_up(board, index + 1, row, col, block):
                #print "true", index, i, j, c
                return True

            else:
                #print "false", index, i, j, c
                board[i][j] = "."
                row[i].remove(c)
                col[j].remove(c)
                block[i / 3 * 3 + j / 3].remove(c)


        return False

    def initilize(self, board, row, col, block):
        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if c == ".":
                    continue
                if c in row[i]:
                    # print "row", i, c
                    return False
                if c in col[j]:
                    # print "col"
                    return False
                if c in block[i / 3 * 3 + j / 3]:
                    # print "block"
                    return False
                row[i].add(c)
                col[j].add(c)
                block[i / 3 * 3 + j / 3].add(c)

        return True
