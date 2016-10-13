"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #dp starts from 1 to n
        if len(s) == 0: return 0
        if s[0]=="0": return 0
        length = len(s)
        dp = [ 0 for i in xrange(length+1)]
        dp[0], dp[1] = 1, 1
        for i in xrange(1, length):
            if s[i]=="0":
                if s[i-1] =="1" or s[i-1]=="2":
                    dp[i+1] = dp[i-1]
                else:
                    return 0
            else:
                dp[i+1] = dp[i]
                if (s[i-1]=="1") or (s[i-1]=="2" and int(s[i])<=6):
                    dp[i+1] += dp[i-1]
        return dp[-1]
