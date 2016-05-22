"""
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

Idea: dynamic programming. Let i, j are the start and end index of a substring, we have:
p(i,j) = p(i-1, j+1) +2 if s[i]==s[j] and p(i+1,j-1)>0
starting point: p(i,i)=1, p(i,i+1)=2 if s[i]==s[i+1]
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #intialize dynamic programming table, dp[start, end]=value, value: length of palindrome; not palindrome: value=-1
        
        length = len(s)
        dp = [   [-1]*length  for i in range(length) ]
        
        #initiallize dp[i,i] and dp[i,i+1]
        start, end = 0, 0
        longest = 1
        #print dp
        for i in range(length):
            dp[i][i]=1
        for i in range(length-1):
            if s[i]==s[i+1]:
                dp[i][i+1] =2
                start, end = i, i+1
        #fill the dp table
        #p(i,j) = p(i-1, j+1) +2 if s[i]==s[j] and p(i+1,j-1)>0
        for i in range(length-1, -1,-1):
            for j in range(i+2, length):
                #print i,j
                if s[i]==s[j] and dp[i+1][j-1]>0:
                    dp[i][j] = dp[i+1][j-1]+1
                    if longest< dp[i][j]:
                        longest = dp[i][j]
                        (start, end) = (i,j)
        return s[start: end+1]
