class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        self.diff_hash = {}
        
        self.result = []
        self.min_length = len(wordlist)+2
        
        cur_res = [beginWord]
        isIn={}
        
        #self.dfs(beginWord, endWord, wordlist, cur_res, isIn)
        self.bfs(beginWord, endWord, wordlist)
        
        return self.result
    
    def bfs(self, beginWord, endWord, wordlist):
        q = []
        cur_list = [beginWord]
        q.append( (cur_list) )
        sucess = 0
        while q:
            (cur_list) = q.pop(0)
            #if len(cur_list) >=self.min_length:
            #    break
            lastword = cur_list[-1]
            #find the shortest ladder
            #print cur_list
            #if (lastword+endWord) in self.diff_hash or self.diff_letter(lastword, endWord):
            if (lastword, endWord) in self.diff_hash or self.diff_letter(lastword, endWord):
                if len(cur_list)< self.min_length:
                    self.result.append( cur_list+[endWord])
                    self.min_length = len(cur_list)+1
                    sucess =1
            if sucess ==1:
                continue
            
            candidate_list = set(wordlist) - set(cur_list)
            for word in candidate_list:
            #for word in wordlist:
                #if word not in cur_list and ((lastword, word) in self.diff_hash or self.diff_letter(lastword, word)):
                if (lastword, word) in self.diff_hash or self.diff_letter(lastword, word):
                #if (lastword+word) in self.diff_hash or self.diff_letter(lastword, word):
                    q.append(  (cur_list+[word]) ) 
        
    
    def dfs(self, beginWord, endWord, wordlist, cur_res, isIn ):
        if len(cur_res) > self.min_length:
            return 
        
        if (beginWord+endWord ) in self.diff_hash or self.diff_letter(beginWord, endWord):
        #if (beginWord, endWord ) in self.diff_hash or self.diff_letter(beginWord, endWord):
        #if self.diff_letter(beginWord, endWord):
            cur_res.append(endWord)
            if len(cur_res) <self.min_length:
                self.result = [cur_res]
                self.min_length=len(cur_res)
            elif len(cur_res) == self.min_length:
                self.result.append(cur_res)
        
        for word in wordlist:
            # not in the current result and edit_dis == 1
            
            if (word not in isIn) and ((word+beginWord ) in self.diff_hash or self.diff_letter(word, beginWord)):
            #if (word not in isIn) and ((word, beginWord ) in self.diff_hash or self.diff_letter(word, beginWord)):
            #if (word not in isIn) and ( self.diff_letter(word, beginWord)):
                #cur_res.append(word)
                isIn[word]=True
                self.dfs( word, endWord, wordlist, cur_res+[word], isIn)
                isIn.pop(word)
        
        
    def diff_letter(self, a, b):
        num = sum( [ 1 for i in range(len(a)) if a[i]!=b[i]])
        if num == 1:
            self.diff_hash[ (a, b) ] = True
            self.diff_hash[ (b, a) ] = True
            #self.diff_hash[ a+b ] = True
            #self.diff_hash[ b+a ] = True
            return True
        return False

def main():
    a = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    
    beginWord ="hot"
    endWord ="dog"
    wordList =["hot","cog","dog","tot","hog","hop","pot","dot"]
    
    beginWord = "qa"
    endWord = "sq"
    wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
    
    result = a.findLadders(beginWord, endWord, wordList)
    print result

if __name__ == "__main__":
    main()
