"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        lists=['']*numRows
        N=(numRows-1)*2
        
        for i in range(len(s)):
            if i==0:
                lists[0] += s[i]
            else:
                k = i%N
                index = min(k, (numRows -1) - (k -numRows +1))
                lists[index]+= s[i]
                
        return ''.join(lists)

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
            
        row = [""]*numRows
        N = (numRows - 1)*2
        for i in xrange(len(s)):
            ch = s[i]
            index = i%N
            if i%N > numRows-1:
                index = N - index
            #print index
            row[index]+=ch
        return "".join(row)  
