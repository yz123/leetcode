#idea: first reverse the word; then reverse the whole string
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #one line python
        #return " ".join(reversed(s.split()))
        length = len(s)
        num = 0
        while num < length:
            while num<length and s[num] == " " :
                num +=1
            if num>=length:
                break
            #TODO
        return self.reverse(s, 0, length-1)
        
    def reverse(self, s, begin, end):
        length = len(s)
        if length>1:
            while begin< end:
                tmp=s[begin]
                s[begin]=s[end]
                s[end]=tmp
                begin +=1
                end -=1
        
        return s
        
"""
        def reverseWords(self, s):
        #one line python
        #return " ".join(reversed(s.split()))
        
        #char = ""
        list = []
        num = 0
        while num<len(s):
            while num<len(s) and s[num] == " " :
                num +=1
            if num>=len(s):
                break
            #not " "
            ch=""
            while  num<len(s) and s[num]!=" ":
                ch += s[num]
                num += 1
            list.insert(0,ch)
            #tmp = "".join(ch)
            #if char !="":
            #    char = " "+char
            #char = tmp + char
                
        #return char
        return " ".join(list)
"""
