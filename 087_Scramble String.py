"""
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
"""

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        return self.dp(s1, s2)
        
        #return self.recursive_search(s1, s2)
    
    #recursive search: divde and conquer
    #"great", "rg tea"
    def recursive_search(self, s1, s2):
        if s1 == s2: return True
        
        if sorted(s1) != sorted(s2): return False
        
        length = len(s1)
        for i in xrange(1, length):
            if self.recursive_search(s1[i:], s2[i:]) and self.recursive_search(s1[:i], s2[:i]):
                return True
            if self.recursive_search(s1[i:], s2[:length-i]) and self.recursive_search(s1[:i], s2[length-i:]):
                return True
        return False
    
    #http://blog.csdn.net/ljiabin/article/details/44537523
    #dp[i][j][k] : range dp[s1][s2][length]
    #表示s1从i开始，s2从j开始，长度为k的子串是否是scramble
    #starting point: dp[i][j][1]=  (if s1[i]=s2[j])
    #recursive: dp[i][j][k] =  for x in (1, k) : dp[i][j][x] and dp[i+k][j+k][k-x]  或者 dp[i][j+ (k-x)][x] and dp[i+x][j][k-x]
    def dp(self, s1, s2):
        
        if sorted(s1)!=sorted(s2): return False
        if s1 == s2: return True
        length = len(s1)
        dp = [ [ [ False for k in xrange(length+1) ] for j in xrange(length)] for i in xrange(length) ]
        
        for i in xrange(length):
            for j in xrange(length):
                dp[i][j][1] = (s1[i]==s2[j])
        
        for k in xrange(2, length+1):
            for i in xrange(length-k+1):
                for j in xrange(length-k+1):
                    
                    for x in xrange(1, k):
                        if ( dp[i][j][x] and dp[i+x][j+x][k-x]) or (  dp[i][j+ (k-x)][x] and dp[i+x][j][k-x]  ):
                            dp[i][j][k]= True
        
        return dp[0][0][length]
        
        
