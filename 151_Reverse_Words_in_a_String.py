"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
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
        
