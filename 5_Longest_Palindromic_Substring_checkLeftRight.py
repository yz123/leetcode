"""
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

Idea: from a current charactoer, check whether left and right is the same
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = 0
        start = 0
        end = 0
        for i in range(len(s)):
            l1 = self.getPalindrome(s, i, i)
            l2 = self.getPalindrome(s, i, i+1)
            #print l1, l2
            l = max(l1, l2)
            #print l
            if l> length:
                length =l
                if l %2 ==0:
                    start = i - l/2 +1
                else:
                    start = i -l/2
                end = i+ l/2
            
        return s[start: end+1]
        
    def getPalindrome(self, s, left, right):
        start = 0
        end = len(s) -1
        while left >= start and right <= end and s[left]==s[right]:
            left -=1
            right +=1
        #print left, right
        l = right - left -1    
        return l
        
