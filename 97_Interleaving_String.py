"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
"""

#https://discuss.leetcode.com/topic/30127/summary-of-solutions-bfs-dfs-dp
#https://discuss.leetcode.com/topic/6562/8ms-c-solution-using-bfs-with-explanation/11
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        #return self.recursion(s1, s2, s3)
        #return self.dp(s1, s2, s3)
        return self.bfs(s1,s2,s3)
    
    #s1: i; s2:j; dp[m+1][n+1]
    #dp[i,0] = dp[i-1, 0] && s1[i-1] == s3[i-1]
    #dp[0, j] = dp[0, j-1] && s2[j-1]==s3[j-1]
    #dp[i,j] = ( dp[i-1,j] && s1[i-1]==s3[i+j-1] )  or ( dp[i,j-1] && s2[j-1]==s3[i+j-1]   )
    def dp(self, s1, s2, s3):
        m = len(s1)
        n = len(s2)
        g = len(s3)
        if m+n !=g: return False
        if m == 0: return s2 == s3
        if n == 0: return s1 == s3
        if g == 0 and m ==0 and n ==0: return True
        
        dp =[ [False]*(n+1)  for i in range(m+1) ]
        dp[0][0] = True
        for i in range(1, m+1):
            dp[i][0] = ( dp[i-1][0] and s1[i-1] == s3[i-1] )
            if dp[i][0] == False: break
        for j in range(1, n+1):
            dp[0][j] = ( dp[0][j-1] and s2[j-1] == s3[j-1]  )
            if dp[0][j] == False: break
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                c1 = ( dp[i-1][j] and s1[i-1]==s3[i+j-1] )
                c2 = ( dp[i][j-1] and s2[j-1]==s3[i+j-1] )
                dp[i][j] = ( c1 or c2 )
                
        return dp[m][n]
    
    #bfs:想象成图的bfs
    #https://discuss.leetcode.com/topic/6562/8ms-c-solution-using-bfs-with-explanation
    def bfs(self, s1, s2, s3):
        m = len(s1)
        n = len(s2)
        g = len(s3)
        if m+n !=g: return False
        if m == 0: return s2 == s3
        if n == 0: return s1 == s3
        if g == 0 and m ==0 and n ==0: return True
        
        hash = {}
        q =[]
        q.append( (0,0) )
        while q:
            (i, j) = q.pop(0)
            if (i,j) in hash:
                continue
            #print (i,j)
            if i> m or j>n:
                break
            if i == m and j == n:
                return True
            
            if j<n and s2[j]==s3[i+j]:
                q.append( (i,j+1))
            if i<m and s1[i] == s3[i+j]:
                q.append( (i+1,j) )

            hash[(i,j)] = True
            
        return False
    
    """
    s1 = "aabcc",
    s2 = "dbbca",
    When s3 = "aadbbcbcac", return true.
    When s3 = "aadbbbaccc", return false.
    """
    def recursion(self, s1, s2, s3):
        m = len(s1)
        n = len(s2)
        g = len(s3)
        if m+n != g:
            return False
        if m == 0:
            return s2==s3
        if n == 0:
            return s1 == s3
        if g == 0:
            if m==0 and n == 0:
                return True
            else:
                return False
        a, b = False, False
        if s3[0]==s1[0]:
            a= self.recursion(s1[1:], s2, s3[1:])
        if s3[0]==s2[0]:
            b= self.recursion(s1, s2[1:], s3[1:])
        if a or b:#https://discuss.leetcode.com/topic/30127/summary-of-solutions-bfs-dfs-dp
#https://discuss.leetcode.com/topic/6562/8ms-c-solution-using-bfs-with-explanation/11
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        #return self.recursion(s1, s2, s3)
        #return self.dp(s1, s2, s3)
        return self.bfs(s1,s2,s3)
    
    #s1: i; s2:j; dp[m+1][n+1]
    #dp[i,0] = dp[i-1, 0] && s1[i-1] == s3[i-1]
    #dp[0, j] = dp[0, j-1] && s2[j-1]==s3[j-1]
    #dp[i,j] = ( dp[i-1,j] && s1[i-1]==s3[i+j-1] )  or ( dp[i,j-1] && s2[j-1]==s3[i+j-1]   )
    def dp(self, s1, s2, s3):
        m = len(s1)
        n = len(s2)
        g = len(s3)
        if m+n !=g: return False
        if m == 0: return s2 == s3
        if n == 0: return s1 == s3
        if g == 0 and m ==0 and n ==0: return True
        
        dp =[ [False]*(n+1)  for i in range(m+1) ]
        dp[0][0] = True
        for i in range(1, m+1):
            dp[i][0] = ( dp[i-1][0] and s1[i-1] == s3[i-1] )
            if dp[i][0] == False: break
        for j in range(1, n+1):
            dp[0][j] = ( dp[0][j-1] and s2[j-1] == s3[j-1]  )
            if dp[0][j] == False: break
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                c1 = ( dp[i-1][j] and s1[i-1]==s3[i+j-1] )
                c2 = ( dp[i][j-1] and s2[j-1]==s3[i+j-1] )
                dp[i][j] = ( c1 or c2 )
                
        return dp[m][n]
    
    #bfs:想象成图的bfs
    #https://discuss.leetcode.com/topic/6562/8ms-c-solution-using-bfs-with-explanation
    def bfs(self, s1, s2, s3):
        m = len(s1)
        n = len(s2)
        g = len(s3)
        if m+n !=g: return False
        if m == 0: return s2 == s3
        if n == 0: return s1 == s3
        if g == 0 and m ==0 and n ==0: return True
        
        hash = {}
        q =[]
        q.append( (0,0) )
        while q:
            (i, j) = q.pop(0)
            if (i,j) in hash:
                continue
            #print (i,j)
            if i> m or j>n:
                break
            if i == m and j == n:
                return True
            
            if j<n and s2[j]==s3[i+j]:
                q.append( (i,j+1))
            if i<m and s1[i] == s3[i+j]:
                q.append( (i+1,j) )

            hash[(i,j)] = True
            
        return False
    
    """
    s1 = "aabcc",
    s2 = "dbbca",
    When s3 = "aadbbcbcac", return true.
    When s3 = "aadbbbaccc", return false.
    """
    def recursion(self, s1, s2, s3):
        m = len(s1)
        n = len(s2)
        g = len(s3)
        if m+n != g:
            return False
        if m == 0:
            return s2==s3
        if n == 0:
            return s1 == s3
        if g == 0:
            if m==0 and n == 0:
                return True
            else:
                return False
        a, b = False, False
        if s3[0]==s1[0]:
            a= self.recursion(s1[1:], s2, s3[1:])
        if s3[0]==s2[0]:
            b= self.recursion(s1, s2[1:], s3[1:])
        if a or b:
            return True
        return False
