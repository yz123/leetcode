"""
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note:
The numbers can be arbitrarily large and are non-negative.
Converting the input string to integer is NOT allowed.
You should NOT use internal library such as BigInteger.
"""

#https://discuss.leetcode.com/topic/30508/easiest-java-solution-with-graph-explanation
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m, n = len(num1), len(num2)
        res = [0]* (m+n)
        for i in xrange(m-1, -1, -1):
            for j in xrange(n-1, -1, -1):
                mul =  ( ord(num1[i])-ord('0') ) * ( ord(num2[j])-ord('0') )
                p1 = i+j
                p2 = i+j+1
                sum = res[p2]+mul
                res[p1] += sum/10
                res[p2] = sum%10
                
        index = 0
        while index<m+n and res[index]==0:
            index += 1
        if index == m+n: return "0"
        
        res_str = map(lambda x:str(x), res[index:])
        return "".join(res_str)
