"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if board == None or word == None or len(board)==0: return False
        
        row = len(board)
        col = len(board[0])
        is_visit = [ [ False for j in xrange(col) ]  for i in xrange(row) ]
        for i in range(row):
            for j in range(col):
                if self.word_search( board, word, i, j, 0, is_visit ):
                    return True
        return False
        
    def word_search(self, board, word, i, j, word_index, is_visit):
        if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0 or is_visit[i][j] or word[word_index]!=board[i][j]:
            return False
            
        if word_index == len(word) - 1: 
            return True
        
        is_visit[i][j] = True
        
        if self.word_search(board, word, i+1, j, word_index+1, is_visit) \
            or self.word_search(board, word, i-1, j, word_index+1, is_visit) \
            or self.word_search( board, word, i, j+1, word_index+1, is_visit) \
            or self.word_search( board, word, i, j-1, word_index+1, is_visit):
                return True
            
        is_visit[i][j] = False
        return False
