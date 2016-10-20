"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""

#https://discuss.leetcode.com/topic/38514/java-not-so-short-but-easy-to-understand-and-kinda-straightforward-solution-13ms

class Solution(object):
   
    def minWindow(self, s, t):
        #:type s: str
        #:type t: str
        #:rtype: str

        if t == "" or s== "": return ""
        
        s_hash = dict.fromkeys(t,0)
        t_hash = {}
        for ch in t:
            t_hash[ch] = t_hash.get(ch, 0)+1
            
        ans = ""
        
        start, end = 0, 0
        count = 0
        while end < len(s):
            #check s[]
            if s[end] in s_hash:
                if s_hash[ s[end] ] < t_hash[ s[end] ]:
                    count += 1
                s_hash[ s[end] ] += 1
                
            #move start to the closest one    
            if count == len(t):
                while start < end:
                    if s[start] in s_hash:
                        #pass the charactor that repated; if find one character that is not repeated, then OK!
                        if s_hash[ s[start] ] == t_hash[ s[start] ]:
                            break
                        s_hash[ s[start] ] -=1
                    start += 1
                #print start, end    
                if ans =="" or end-start+1 < len(ans):
                    ans = s[start:end+1]
                
                s_hash[ s[start] ] -= 1    
                count -= 1
                start +=1
                
            end += 1
            
        return ans
        
    """    
    def minWindow(self, source, target):
        if (target == ""):
            return ""
        S , T = source, target
        d, dt = {}, dict.fromkeys(T, 0)
        for c in T: d[c] = d.get(c, 0) + 1
        pi, pj, cont = 0, 0, 0
        if (source =="" or target ==""):
            return ""
        ans = ""
        while pj < len(S):
            if S[pj] in dt:
                if dt[S[pj]] < d[S[pj]]:
                    cont += 1
                dt[S[pj]] += 1;
            if cont == len(T):
                while pi < pj:
                    if S[pi] in dt:
                        if dt[S[pi]] == d[S[pi]]:
                            break;
                        dt[S[pi]] -= 1;
                    pi+= 1
                if ans == '' or pj - pi < len(ans):
                    ans = S[pi:pj+1]
                dt[S[pi]] -= 1
                pi += 1
                cont -= 1
            pj += 1
        return ans
     """
    
