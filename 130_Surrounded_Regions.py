"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
"""

#can use either DFS or BFS
#http://www.cnblogs.com/higerzhang/p/4149040.html
#set the boarder "O" to be "#", then replace the other with X
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        length = len(board)
        m = len(board[0])
        #print length, m
        q = board
        for i in range(m):
            if q[0][i] == "O":
                q[0][i] = "#"
                self.dfs(q, 0, i)

            if q[length-1][i] == "O":
                q[length-1][i] = "#"
                self.dfs(q, length-1, i)
        
        for j in range(1, length-1):
            if q[j][0] == "O":
                q[j][0] = "#"
                self.dfs(q, j, 0)

            if q[j][m-1] == "O":
                q[j][m-1] = "#"
                self.dfs(q, j, m-1)
        
        for i in range(length):
            for j in range(m):
                if q[i][j] =="#":
                    q[i][j]= "O"
                elif q[i][j] == "O":
                    q[i][j] = "X"
    
    #search whether it is surrounded by "O"    
    def dfs(self, board, i, j):
        
            
        row = len(board)
        col = len(board[0])
        
        if i > 1 and board[i-1][j] == 'O':
            board[i-1][j] = '#'
            self.dfs(board, i-1, j)
        
        if i< row-1 and board[i+1][j] == 'O':
            board[i+1][j] = '#'
            self.dfs(board, i+1, j)
        
        if j > 1 and board[i][j-1] == 'O':
            board[i][j-1] = '#'
            self.dfs(board, i, j-1)
            
        if j < col-1 and board[i][j+1] == 'O':
            board[i][j+1] = '#'
            self.dfs(board, i, j+1)

#BFS            
"""
// Method 1 BFS  
public class Solution {  
    public void solve(char[][] board) {  
        if (board == null || board.length == 0 || board[0].length == 0)  
            return;  
        int m = board.length, n = board[0].length;  
        for (int j = 0; j < n; j++) {  
            if (board[0][j] == 'O') bfs(0, j, board); // row 0  
            if (board[m - 1][j] == 'O') bfs(m - 1, j, board); // last row  
        }  
        for (int i = 0; i < m; i++) {  
            if (board[i][0] == 'O') bfs(i, 0, board); // col 0  
            if (board[i][n - 1] == 'O') bfs(i, n - 1, board); // last col  
        }  
          
        for (int i = 0; i < m; i++) {  
            for (int j = 0; j < n; j++) {  
                if (board[i][j] == 'O') board[i][j] = 'X';  
                else if (board[i][j] == 'M') board[i][j] = 'O';  
            }  
        }  
    }  
    public void bfs(int i, int j, char[][] board) {  
        LinkedList<Integer> queue = new LinkedList<Integer>();  
        visit(i, j, board, queue);  
        while (!queue.isEmpty()) {  
            int idx = queue.poll();  
            int r = idx / board[0].length;  
            int c = idx % board[0].length;  
            visit(r - 1, c, board, queue);  
            visit(r + 1, c, board, queue);  
            visit(r, c - 1, board, queue);  
            visit(r, c + 1, board, queue);  
        }  
    }  
    public void visit(int i, int j, char[][] board, LinkedList<Integer> queue) {  
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || board[i][j] != 'O')  
            return;  
        board[i][j] = 'M';  
        queue.offer(i * board[0].length + j);  
    }  
}  
"""
