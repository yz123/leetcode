#https://discuss.leetcode.com/topic/53451/4-liner-in-python
"""
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""


class Solution(object):
    
    """
    #time complexity: O(|s|^3: |s| for slice)
    def wordBreak(self, s, wordDict):
        map = {}
        for w in wordDict:
            map[w] = True
        lens = len(s)
        dp = [ False for i in range(lens+1) ]
        dp[0] = True
        for i in range(1, lens+1):
            for j in range(i):
                if dp[j] and ( s[j:i] in map ):
                    dp[i] = True
        return dp[lens]
    """
    
    #time complexity: O(|w||s|^2: |s| for slice)
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        map = {}
        for w in wordDict:
            map[w] = True
        lens = len(s)
        dp = [ False for i in range(lens+1) ]
        dp[0] = True
        for i in range(1, lens+1):
            for w in map:
                lenw = len(w)
                if i >= lenw and dp[i-lenw] and s[i-lenw:i]==w:
                    dp[i]=True
                    break
        return dp[lens]
