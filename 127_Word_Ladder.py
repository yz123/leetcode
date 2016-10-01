#http://www.cnblogs.com/yrbbest/p/4438488.html
#bi-bfs

"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
"""

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        #return self.bfs(beginWord, endWord, wordList)
        return self.bi_bfs(beginWord, endWord, wordList)
    
    def bfs(self, beginWord, endWord, wordList):
        q=[]
        #isIn={}
        #isIn[beginWord]=True
        q.append( (beginWord, 1) )
        while q:
            (word, level) = q.pop(0)
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if word[i]!=c:
                        new_word = word[:i] + c + word[i+1:]
                        #if new_word not in isIn and new_word in wordList:
                        if  new_word in wordList:
                            if new_word == endWord:
                                return level+1
                            q.append( (new_word, level+1) )
                            #isIn[new_word]=True
                            wordList.remove(new_word)
        
        return 0
    
    def bi_bfs(self, beginWord, endWord, wordList):
        begin_set =set()
        end_set = set()
        wordset = set(wordList)
        
        begin_set.add( (beginWord) )
        end_set.add( (endWord) )
        step = 2
        while len(begin_set)>0 and len(end_set)>0:
            if len(begin_set) > len(end_set):
                tmp = end_set
                end_set = begin_set
                begin_set = tmp
            tmp = set()
            for word in begin_set:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if word[i]!=c:
                            new_word = word[:i] + c + word[i+1:]
                            if new_word in end_set:
                                return step
                            if new_word in wordset:
                                tmp.add(new_word)
                                wordset.remove(new_word)
            begin_set = tmp                
            step +=1        
        
        return 0
