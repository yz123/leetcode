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
   (1) s[: i-1] match p[:j-1]: True
   (2) s[: i] match p[:j-1]: True
   (3) s[: i] match p[:j-2]: j>=1 True
   (4) s[: i-1] match p[:j]:  check whether s[i]==p[j-1] (j>=1)
   
"""
