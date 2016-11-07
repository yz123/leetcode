"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        """
        #depth <=4 , valid
        self.res = []
        path = ""
        self.dfs_backtracking(s, path, 0)
        return self.res
        """
        return self.dp(s)
    
    #dp[j]= 
    def dp(self, s):
        if (not s) or len(s) ==0 or len(s)>12: return []
    
        length = len(s)
        dp = [ None for i in range(length+1)]
        dp[0]=[[""]]
        #dp[1] = [s[0]]
        
        for cur in range(length):
            for j in range(3):
                if cur >= j:
                    begin = cur-j
                    if dp[begin]:
                        sub = s[begin:cur+1]
                        if sub=="0" or ( sub[0]!="0" and 0<=int(sub)<=255):
                            if not dp[cur+1]:
                                dp[cur+1]=[]
                            for strr in dp[begin]:
                                #if len(strr)<=4:
                                dp[cur+1].append(strr+[sub] )
        
        #for i in range(len( dp)):
        #    print i,
        #    for ll in dp[i]:
        #        print ".".join(ll[1:])
            
        res =[]    
        for str_list in dp[-1]:
            str_list =str_list[1:]
            if len(str_list) == 4:
                res.append(".".join(str_list))
        return res
    
    #backtracking:
    #if s[:i-1] is valid, 则看后面是否是valide
    def dfs_backtracking(self, s, path, depth):
        if (not s) or len(s) == 0 or len(s)>12: return
        #end condition
        if depth==3 and len(s)<=3 and ( s=="0" or (s[0]!="0" and  0<=int(s)<=255) ):
            path +=s
            self.res.append(path)
        
        length = len(s)
        for i in range(3):
            if i<length:
                pre, sur = s[:i+1], s[i+1:]
                if  pre=="0" or ( s[0]!="0" and  0<=int(pre)<=255):
                    #print path
                    self.dfs_backtracking(sur, path+pre+".", depth+1)
