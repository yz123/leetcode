"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        return self.bit_operation(n,k)
        
        
        return self.recursion(n,k)
        
        return self.backtracking_bfs(n, k)
        
        self.res = []
        cur_path = []
        cur_index = 0
        self.backtracking_dfs(n, k, cur_path, cur_index)
        return self.res
        
        
    #bit operation
    def bit_operation(self, n,k):
        valid_bit = []
        for i in xrange(1<<n):
            #get number of 1's
            count = 0
            for bit in xrange(n):
                if ( i>>bit & 1 ) == 1:
                    count +=1
            if count == k:
                valid_bit.append(i)
        
        res = []
        for num in valid_bit:
            ans = []
            for i in xrange(n):
                if ( num>>i & 1 ) == 1:
                    ans.append( i+1)
            res.append(ans)
        return res
    
    #dfs backtracking    
    def backtracking_dfs(self, n, k, cur_path, cur_index):
        #print len(cur_path)
        if len(cur_path)==k:
            self.res.append(cur_path)
        else:
            #prune
            upper = n+1 - (k-len(cur_path)) 
            for i in range(cur_index, upper):
                self.backtracking_dfs(n, k, cur_path+[i+1], i+1)
    
    #build a serach tree, prune
    def backtracking_bfs(self, n, k):
        if k > n: return []
        
        q = []
        next_index = 0
        q.append( ([],0  ) )
        #do k iterations for the q
        for level in range(k):
            tmp = []
            for item in q:
                (pre, cur_index) = item
                upper = n+1 - (k - len(pre))
                for j in xrange(cur_index, upper):
                    tmp.append( ( pre+[j+1],  j+1))
            q= tmp
            
        res = []
        while q:
            (sol, index)=q.pop(0)
            res.append(sol)
        return 
    
    #C(n,k) = C(n-1,k-1)+C(n-1,k)
    #C(n, 1) = [[1], [2],[3], ... ], C(n,n) = [  [1,..n]]
    def recursion(self, n,k):
        res = []
        if k == 1:
            for i in xrange(1, n+1):
                res.append([i])
        elif k ==n:
            ans = range(1, n+1)
            res.append(ans)
        else:
            res = self.recursion(n-1, k) #without n
            tmp = self.recursion(n-1, k-1) #with n 
            tmp = [ item+[n] for item in tmp]
            res = res + tmp
            
        return res
        
