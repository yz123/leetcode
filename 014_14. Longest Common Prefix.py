"""
Write a function to find the longest common prefix string amongst an array of strings.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        return self.trie_method(strs)
        return self.horizontal_scan(strs)
    
    def trie_method(self, strs):
        trie = {}
        for s in strs:
            if len(s) == 0:
                return ""
            layer = trie
            for ch in s:
                if ch not in layer:
                    layer[ch] ={}
                layer = layer[ch]
            layer["ch"] = "end" 
        lcp = ""
        layer = trie
        while len(layer) ==1 and ( "ch" not in layer):
            for key in layer:
                lcp += key
                layer = layer[key]
        return lcp
    
    def horizontal_scan(self, strs):
        if not strs:
            return ""
        lcp = strs[0]
        for s in strs[1:]:
            #print s
            i, j = 0, 0
            while i<len(lcp) and j<len(s):
                if lcp[i] == s[j]:
                    i+=1
                    j+=1
                else:
                    break
            lcp = lcp[:i]
                
        return lcp
            
