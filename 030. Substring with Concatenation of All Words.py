"""
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""

class Solution(object):
    def findSubstring(self, s, words):
        #:type s: str
        #:type words: List[str]
        #:rtype: List[int]
        
        return self.find_substring(s, words)
        
        #return self.find_sub(s, words)
        
    def find_substring(self, s, words):
        w_hash = {}
        for word in words:
            w_hash[word] = w_hash.setdefault(word, 0)+1
        wl = len(words[0])
        ans = []
        
        for i in xrange(wl):
            left = i
            right = i
            count = 0
            s_hash = {}
            while right <= len(s)-wl:
                substr = s[right: right+wl]
                if substr in w_hash:
                    if s_hash.setdefault(substr,0)  < w_hash[substr]:
                        count += 1
                        s_hash[substr] += 1
                        if count == len(words):
                            ans.append(left)
                            s_hash[ s[left: left+ wl] ] -= 1
                            count -= 1
                            left = left + wl
                    else:
                        l_str = s[left: left +wl]
                        
                        
                        while l_str!= substr:
                            s_hash[ l_str ] -= 1
                            count -= 1
                            left += wl
                            l_str = s[left: left +wl]
                            
                        #l_str == substr
                        left = left + wl
                        print left, right
                        
                    
                else:
                    count = 0
                    left = right + wl
                    s_hash = {}
                
                right += wl
        
        return  ans
        
    def find_sub(self, s, words):
        w_hash = {}
        for word in words:
            w_hash[word] = w_hash.setdefault(word, 0)+1
        wl = len(words[0])
        ans = []
        
        for i in xrange(wl):
            left = i
            s_hash = {}
            right = i
            count = 0
            while right <= len(s)-wl:
                substr = s[right: right+wl]
                #check if substr is in the words, if not, move to the next work, reset the count and s_hash
                if substr in w_hash:
                    s_hash[substr] = s_hash.setdefault(substr,0) + 1
                    #如果words里面还有substr没出现，就继续
                    if s_hash[substr]<= w_hash[substr]:
                        count +=1
                    else:
                        while s_hash[substr] > w_hash[substr]:
                            s_hash[ s[left:left+wl ] ] -= 1
                            if s_hash[ s[left:left+wl ]]  < w_hash[ s[left:left+wl ]]:
                                count -= 1
                            left += wl
                            
                        """   
                        left_str = s[left: left+wl]
                        while left_str!=substr:
                            left += wl
                            s_hash[left_str] -= 1
                            count -= 1
                            left_str = s[left: left+wl]
                        count -= 1
                        s_hash[left_str] -= 1
                        left += wl
                        """
                    
                    if count == len(words):
                        #print left, right
                        print s[left: left+wl], left, right
                        ans.append(left)
                        count -= 1
                        s_hash[ s[left: left+wl] ] -= 1
                        left += wl
                else:
                    left = right + wl
                    count = 0
                    s_hash = {}
                    
                right += wl  
                
        return ans

    """
    def findSubstring(self, s, words):
    	if len(words) == 0:
    		return []
    	# initialize d, l, ans
    	l = len(words[0])
    	d = {}
    	for w in words:
    		if w in d:
    			d[w] += 1
    		else:
    			d[w] = 1
    	i = 0
    	ans = []
    
    	# sliding window(s)
    	for k in range(l):
    		left = k
    		subd = {}
    		count = 0
    		for j in xrange(k, len(s)-l+1, l):
    			tword = s[j:j+l]
    			# valid word
    			if tword in d:
    				if tword in subd:
    					subd[tword] += 1
    				else:
    					subd[tword] = 1
    				count += 1
    				while subd[tword] > d[tword]:
    					subd[s[left:left+l]] -= 1
    					left += l
    					count -= 1
    				if count == len(words):
    					ans.append(left)
    			# not valid
    			else:
    				left = j + l
    				subd = {}
    				count = 0
    
    	return ans
    """
