#use union-find: initialize, find, union
#http://blog.csdn.net/dm_vincent/article/details/7655764
#http://likesky3.iteye.com/blog/2240270

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

#use union-find: initialize, find, union
#http://blog.csdn.net/dm_vincent/article/details/7655764
#http://likesky3.iteye.com/blog/2240270

======================================================================
#code

// Method 2: Union Find  
public class Solution {  
    public void solve(char[][] board) {  
        if (board == null || board.length == 0 || board[0].length == 0)  
            return;  
        int rows = board.length, cols = board[0].length;  
        int oRoot = rows * cols;  
        initUnionFind(rows * cols);  
        for (int i = 0; i < rows; i++) {  
            for (int j = 0; j < cols; j++) {  
                if (board[i][j] == 'X') continue;  
                int curr = i * cols + j;  
                if (i == 0 || i == rows - 1 || j == 0 || j == cols - 1) {  
                    union(curr, oRoot);  
                } else {  
                    if (j + 1 < cols && board[i][j + 1] == 'O')  
                        union(curr, i * cols + j + 1);  
                    if (j - 1 >= 0 && board[i][j - 1] == 'O')  
                        union(curr, i * cols + j - 1);  
                    if (i + 1 < rows && board[i + 1][j] == 'O')  
                        union(curr, (i + 1) * cols + j);  
                    if (i - 1 >= 0 && board[i - 1][j] == 'O')  
                        union(curr, (i - 1) * cols + j);  
                }  
            }  
        }  
        for (int i = 0; i < rows; i++) {  
            for (int j = 0; j < cols; j++) {  
                if (board[i][j] == 'O' && find(i * cols + j) != oRoot) {  
                    board[i][j] = 'X';  
                }  
            }  
        }  
    }  
    int[] s;  
    int[] rank;  
    private void initUnionFind(int n) {  
        s = new int[n + 1];  
        rank = new int[n + 1];  
        for (int i = 0; i <= n; i++)  
            s[i] = i;  
        rank[n] = n + 1;  
    }  
    private int find(int p) {  
        if (s[p] == p) return p;  
        else return s[p] = find(s[p]);  
    }  
    private void union(int p, int q) {  
        int pRoot = find(p), qRoot = find(q);  
        if (pRoot == qRoot) return;  
        if (rank[pRoot] < rank[qRoot]) {  
            s[pRoot] = qRoot;  
        } else {  
            if (rank[pRoot] == rank[qRoot])  
                rank[pRoot]++;  
            s[qRoot] = pRoot;  
        }  
    }  
} 


======================================================================
#data-structure:

public class UF  
{  
    private int[] id; // access to component id (site indexed)  
    private int count; // number of components  
    public UF(int N)  
    {  
        // Initialize component id array.  
        count = N;  
        id = new int[N];  
        for (int i = 0; i < N; i++)  
            id[i] = i;  
    }  
    public int count()  
    { return count; }  
    public boolean connected(int p, int q)  
    { return find(p) == find(q); }  
    public int find(int p)  
    { return id[p]; }  
    public void union(int p, int q)  
    {   
        // 获得p和q的组号  
        int pID = find(p);  
        int qID = find(q);  
        // 如果两个组号相等，直接返回  
        if (pID == qID) return;  
        // 遍历一次，改变组号使他们属于一个组  
        for (int i = 0; i < id.length; i++)  
            if (id[i] == pID) id[i] = qID;  
        count--;  
    }  
}  
