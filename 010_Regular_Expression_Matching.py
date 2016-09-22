"""
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") ? false
isMatch("aa","aa") ? true
isMatch("aaa","aa") ? false
isMatch("aa", "a*") ? true
isMatch("aa", ".*") ? true
isMatch("ab", ".*") ? true
isMatch("aab", "c*a*b") ? true
"""
'''
https://discuss.leetcode.com/topic/48918/a-pattern-based-dp-solution-in-c-best-submission-4ms/4
Idea: 
1. check if len(p)==1, if it is, check *; 
2. if len(p)>1: check whether 
        (1) p is like "a*XX", if not, check s[0]==p[0], move both to next char; 
        (2) if p is like "a*XX", 
             *check isMatch(s, "XX")==True, 
             *if not, check if p[0]==s[0], if true, move to isMach(s[1:], p)
'''


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
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

def main():
    a = Solution()
    if a.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c") == False:
        print "False"
    else:
        print "True"

if __name__=="__main__":
    main()
