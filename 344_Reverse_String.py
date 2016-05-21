class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        #return ''.join(reversed(s))
        #return s[::-1]
        
        n=len(s)
        if n<2:
            return s
        else:
            slist = list(s)
            start, end = 0, n-1
            while start < end:
                slist[start], slist[end] = slist[end], slist[start]
                start +=1
                end -=1
            return ''.join(slist)
