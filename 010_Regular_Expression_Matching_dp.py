"""
http://blog.csdn.net/fzzying3/article/details/42057935
http://www.cnblogs.com/zuoyuan/p/3781773.html
dp[s][p]
dp[0][0]=True
dp[i+1][0]=False
dp[0][j+1]= True if dp[0][j]==True and p[j]=="*"

s=[XXX i-2 i-1 i]
p=[XXX j-2 j-1 j]
dp[i+1][j+1]= 

   if j not *: dp[i][j] == True and  (p[j]=. or p[j]==s[i])
   if j == * : 
   
   s=[XXX i-2 i-1 i]
   p=[XXX j-2 j-1 *]
   (2) s[: i] match p[:j-1]: True
   (3) s[: i] match p[:j-2]: j>=1 True
   (4) s[: i-1] match p[:j]:  check whether s[i]==p[j-1] (j>=1)
   
"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        slen = len(s)
        plen = len(p)
        dp = [ [False for j in range(plen+1)] for i in range(slen+1)]
        
        #initialize
        dp[0][0]=True
        for j in range(plen):
            if p[j]=="*" and j>=1 and dp[0][j-1]==True:
                dp[0][j+1]=True
        
        for i in range(slen):
            for j in range(plen):
                if p[j] != "*":
                    #if dp[i][j] == True and (p[j]=="." or p[j]==s[i] ):
                    #    dp[i+1][j+1] = True
                    dp[i+1][j+1] = ( dp[i][j] and (p[j]=="." or p[j]==s[i] )  )
                else:
                    dp[i+1][j+1] = (  dp[i+1][j] or ( j>=1 and dp[i+1][j-1]) or ( j>=1 and dp[i][j+1] and (p[j-1]=="." or p[j-1]==s[i] )) )
        
        return dp[slen][plen]
        
"""
class Solution(object):
    def isMatch(self, s, p):
        return self.matching(s, p)
        
    def matching(self, s, p):    
        slen = len(s)
        plen = len(p)
        if plen ==0:
            if slen == 0:
                return True
            else:
                return False    
        else: #the len of p is not 0
            if plen==1: 
                if p[0] == "*": #check whether p="*"
                    return True
                elif slen!=0 and (p[0] == "." or p[0] == s[0]):
                    return self.matching(s[1:], p[1:])
                else:    
                    return False
            else: # plen >1
                if p[1]!="*":
                    if slen!=0 and (p[0] == "." or p[0] == s[0]):
                        return self.matching(s[1:], p[1:])
                    elif slen!=0 and (p[0]=="*"):
                        return (  self.matching(s[1:], p[1:]) or self.matching(s[1:], p)  )
                    else: 
                        return False
                else: #p="a* XXX"
                    if self.matching(s, p[2:]) == True:
                        return True
                    else:
                        if slen!=0 and (p[0] == "." or p[0] == s[0]):
                            return self.matching(s[1:],p)
                        else:
                            return False
"""

def main():
    a = Solution()
    #if a.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c") == False:
    #if a.isMatch("aab", "c*a*b") == False:
    if a.isMatch("aaba", "ab*a*c*a") == False:
        print "False"
    else:
        print "True"

if __name__=="__main__":
    main()
      
################################
#latest version
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        #dp[0][0] = True; dp[j][0] = False
        #dp[0][j] = True if p[j-1]=="*" and dp[0][j-1] = True
        
        slen, plen = len(s), len(p)
        dp = [ [False]*(plen+1) for i in xrange(slen+1) ]
        dp[0][0] = True
        for i in xrange(1, plen+1):
            if i>=2 and p[i-1] == "*" and dp[0][i-2] == True:
                dp[0][i] = True
        
        for i in xrange(1, slen+1):
            for j in xrange(1, plen+1):
                if p[j-1] != "*":
                    if (dp[i-1][j-1]) and (p[j-1] =="." or s[i-1]==p[j-1]):
                        dp[i][j] = True
                        
                else: #p[j-1] == "*"
                    #if dp[i][j-1] or  ( j>=2 and dp[i][j-2]) or (  j>=2 and dp[i-1][j] and  (p[j-2]=="." or p[j-2]==s[i-1])   ):
                    if  ( j>=2 and dp[i][j-2]) or (  j>=2 and dp[i-1][j] and  (p[j-2]=="." or p[j-2]==s[i-1])   ):
                        dp[i][j] = True
        #print dp
        return dp[slen][plen]
