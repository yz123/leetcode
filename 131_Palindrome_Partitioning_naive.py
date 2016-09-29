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
        ans = []
        result = []
        self.dfs(s, ans, result)

        return ans
        
    def dfs(self, s, ans, result):
        if len(s) ==0:
            ans.append(result)
        for i in range(len(s)):
            prefix, surfix = s[:i+1], s[i+1:]
            #print prefix
            if self.isPalindrome(prefix):
                #tmp = result+[prefix]
                #self.dfs(surfix, ans, tmp)
                self.dfs(surfix, ans, result+[prefix])
            
    
    def isPalindrome(self, s):
        length = len(s)
        for i in range(length/2):
            if s[i]!= s[length-1-i]:
                return False
        return True
