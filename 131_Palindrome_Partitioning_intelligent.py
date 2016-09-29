"""
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
For example, given s = "aab",
Return
[
  ["aa","b"],
  ["a","a","b"]
]
"""

#http://www.jianshu.com/p/0f1ee51f400c
#https://discuss.leetcode.com/topic/52156/easy-to-understand-neat-and-modular-java-solution-comments-included
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        return self.dfs(s)

    def dfs(self, s):
        res = []
        if len(s) == 0:
            return [ [] ]
        for i in range(len(s)):
            #if self.isPalindrome(s[:i+1]):
            if s[:i+1] == s[i::-1]:
                get = self.dfs(s[i+1:])
                for ele in get:
                    res.append([s[:i+1]]+ele)
        return res
    
    def isPalindrome(self, s):
        length = len(s)
        for i in range(length/2):
            if s[i]!= s[length-1-i]:
                return False
        return True
