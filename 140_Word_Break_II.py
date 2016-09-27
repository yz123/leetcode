"""
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        map = {}
        for w in wordDict:
            map[w] = True
        
        lens = len(s)
        dp = [ False for i in range(lens+1) ]
        dp[0] = [""]
        
        for i in range(1, lens+1):
            for w in map:
                lenw = len(w)
                if i>=lenw and dp[i-lenw]!=False and s[i-lenw: i] ==w:
                    if dp[i]!= False:
                        dp[i].append(w)
                    else:
                        dp[i]=[w]
        #print dp
        solution =self.backtracking(dp, lens)
        return solution
    
    def backtracking(self, dp, index):
        solution = []
        if index == 0:
            return [""]
        if dp[index] !=False:
            #print index
            for w in dp[index]:
                #print w, index
                if index >= len(w):
                    li = self.backtracking(dp, index-len(w))
                    for word in li:
                        #print word
                        if word!= "":
                            solution.append( word+" "+w)
                        else:
                            solution.append( w)
        return solution    
