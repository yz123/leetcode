"""
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

click to show corner cases.

Corner Cases:
A line other than the last line might contain only one word. What should you do in this case?
In this case, that line should be left-justified.
"""

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words: return []
        
        result, length = [], 0
        cur = []
        for i in range(len(words)):
            w = words[i]
            # word_length + space
            if len(w) + length + len(cur) <= maxWidth:
                cur.append(w)
                length += len(w)
            else:
                if len(cur) ==1:
                    result.append(cur[0]+" "*(maxWidth-len(cur[0])))
                else:
                    space = maxWidth - length
                    #print space
                    between_word = space / ( len(cur)-1)
                    #print between_word
                    extra = space % (len(cur)-1)
                    for i in range(extra):
                        cur[i]= cur[i]+" "
                    result.append( (" "*between_word).join(cur) )
                
                cur = [w]
                length = len(w)
        
        result.append( " ".join(cur)+" "* (maxWidth-length-len(cur)+1) )            
        return result        
        
