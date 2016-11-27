"""
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.two_pointers(s, p)
        return self.dp(s, p)
    
    #d[0, j] =  False if d[0, j-1] == False; True if d[0, j-1] and s[j]=="*"
    #d[i, 0] = False if d[i-1, 0] = False
    #if p[j] == "*" and (dp[i-1][j-1] or dp[i][j-1] or dp[i-1][j]): then dp[i][j] = True
    #if dp[i-1][j-1] and (p[j] == s[i] or p[j] == "?"): then dp[i][j] = True
    def dp(self, s, p):
        if len(s)==0 and len(p)==0: return True
        
        dp = [ [ False for j in xrange(len(p)+1)] for i in xrange(len(s)+1)]
        dp[0][0] = True
        for j in xrange(1, len(p)+1):
            if dp[0][j-1] and p[j-1] == "*":
                dp[0][j] = True
        
        for i in xrange(1, len(s)+1):
            for j in xrange(1, len(p)+1):
                if p[j-1]=="*" and (dp[i-1][j-1] or dp[i][j-1] or dp[i-1][j]):
                    dp[i][j] = True
                else:
                    if dp[i-1][j-1] and (p[j-1] == s[i-1] or p[j-1] == "?"):
                        dp[i][j] = True
        
        return dp[-1][-1]
    
    #https://discuss.leetcode.com/topic/3040/linear-runtime-and-constant-space-solution
    #https://discuss.leetcode.com/topic/66829/18-line-python-backtracking-beats-85
    """
    There are two special symbols '?' and '*'.
    '?' makes no additional difficult, since it matches any single character.
    '*' makes all the problems or say possibilities of different matching.

    Therefore, we use one extra pointer indicating the location of the latest '*'. When ever a match fails, we fall back to the latest '*'.
    """
    def two_pointers(self, s, p):
        if len(s)==0 and len(p)==0: return True
        s_length = len(s)
        p_length = len(p)
        i, j = 0, 0
        back_i, back_j = s_length, 0
        while i<s_length:
            if (j<p_length) and (s[i] == p[j] or p[j] == "?"):
                i += 1
                j += 1
            elif (j<p_length) and p[j]=="*":
                back_i, back_j = i, j
                j += 1
            elif back_i < s_length:
                i, j = back_i+1, back_j+1
                back_i += 1
            else: 
                return False
         
        while j<p_length and p[j]=="*":
            j+=1
        if j == p_length:
            return True
        else:
            return False
