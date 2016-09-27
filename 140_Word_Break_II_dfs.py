class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        dfe idea: 如果s在dict中，return s; 否则，把s分成两半,进行遍历 
        """
        tokenDict = {}
        def dfs(s):
            ans = []
            if s in wordDict:
                ans.append(s)
            #如果i取len(s),s[:i+1]就是整个字符，前面已经check过了
            for i in range(len(s)-1):
                prefix, suffix = s[:i+1], s[i+1:]
                #prefix匹配，匹配，看后面
                if prefix in wordDict:
                    if suffix in tokenDict:
                        rest = tokenDict[suffix]
                    else:
                        rest = dfs(suffix)
                    for word in rest:
                        ans.append(prefix + " " + word)
            #tokenDict[s]=ans
            return ans
        
        
        return dfs(s)
