"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""

#http://fisherlei.blogspot.com/2013/03/leetcode-palindrome-partitioning-ii.html
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        #from beginning to end
        #d[i] =min(d[i], 1+d[j-1]) if j ---- i is Palindrome
        length = len(s)
        
        d = [ i-1 for i in range(length+1)]
        P =[ [ False for j in range(length)] for i in range(length)  ]
        for i in range(length):
            for j in range(i+1):
                if s[i] == s[j] and (i-j<2 or P[i-1][j+1]):
                    P[i][j]=True
                    d[i+1] = min( d[i+1], 1+d[j])
        #print d[0], d[1],d[2],d[3]
        return d[-1]
        """
        #from end to beginning
        
        length = len(s)
        #d[i]: i to n的cut
        d =[length-i-1 for i in range(length+1) ]
        P =[ [ False for j in range(length)] for i in range(length)  ]
        for i in range(length-1, -1, -1):
            for j in range(i, length):
                if s[i] == s[j] and (j-i<2 or P[i+1][j-1]):
                    P[i][j]=True
                    d[i] = min( d[i], 1+d[j+1])
        return d[0]
        """
        
