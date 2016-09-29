# d[i] = min ( i,  min( d[j]+1 [if j+1---i is palindrome ] )  )
# d[i] = i : initial value
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        d = [ i for i in range(length)]
        for i in range(length):
            if s[:i+1] == s[i::-1]:
                d[i] = 0
                
        # d[i] = min ( i,  min( d[j]+1 [if j+1---i is palindrome ] )  )
        for i in range(1, length):
            #print d[i]
            for j in range(i):
                # if j+1 === i is palindrome
                if s[ j+1:i+1]==s[i:j:-1]:
                    d[i] = min( d[i], d[j]+1)
            
        return d[length -1]
