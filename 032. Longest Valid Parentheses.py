"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # dp[i] longest parentnesses to the index i
        # dp[0] = 0
        # if s[i] == "(" dp[i] == 0
        # if s[i] == ")": check s[i]-1: 
           #if it is "(": then dp[i] = dp[i-2]+2
           #if it is ")" and s[i - dp[i-1]-1 ] == "(": then dp[i] = 1+ dp[i-1] + 1 + dp[ i-dp[i-1]-2  ]
        if len(s)<1:
            return 0
        length = len(s)
        dp = [0 for i in xrange(length)]
        for i in xrange(1, length):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = 2 + (dp[i-2] if i-2>=0 else 0)
                else:
                    if i - dp[i-1]-1>=0 and s[i - dp[i-1]-1 ] == "(":
                        dp[i] = 2 + dp[i-1] + ( dp[ i-dp[i-1]-2  ] if i-dp[i-1]-2 >=0 else 0)
        return max(dp)
