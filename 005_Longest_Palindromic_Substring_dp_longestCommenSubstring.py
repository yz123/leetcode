class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #get t by reversing s
        #s = fbcbae, t=eabcbf 
        #dp for the longest common substring: LCS(i,j) = LCS(i-1,j-1)+1 if s[i]==t[j] else LCS(i,j)=0; starting: LCS(i,0)=1 if s[i]=t[0]
        # for the palindrome: 
        # LCS(i,j) = LCS(i-1,j-1)+1 if s[i]==t[j] and len(t)-j= i-( LCS(i-1,j-1)+1)+1 else LCS(i,j)=0; 
        #  starting: LCS(i,0)=1 if s[i]=t[0] and i+j=len(s)-1; LCS(0,j) =1 if s[0]=t[j] and i+j=len(s)-1
        length = len(s)
        dp = [ [0]*length for i in range(length) ]
        t=s[::-1]
        #print t
        for i in range(length):
            if s[i]==t[0]:
                dp[i][0]=1
            if s[0]==t[i]:
                dp[0][i]=1
        
        longest=1
        end =0
        for i in range(1, length):
            for j in range(1,length):
                if s[i] == t[j] :
                    dp[i][j]=dp[i-1][j-1]+1
                    if dp[i][j]>longest and length-j-1 == i - dp[i-1][j-1] :
                        end =i
                        longest=dp[i][j]
        start = end-longest+1
        return s[start: end+1]
