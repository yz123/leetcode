"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return self.mapping(a,b)
        
        return self.convert_to_int(a,b)
        
        return self.simple(a,b)
    
    def simple(self, a,b):
        aa = int(a, 2)
        bb = int(b, 2)
        #print bin(aa+bb)
        return str(bin(aa+bb))[2:]
        
    def convert_to_int(self, a,b):
        aa, bb = 0, 0
        for i in a:
            aa = int(i) + (aa<<1)
        for i in b:
            bb = int(i) + (bb<<1)
        
        c = aa + bb
        res = ""
        if c ==0:
            return "0"
        while c:
            b = c%2
            c = c/2
            res = str(b) + res
        return res
        
    def mapping(self, a,b):
        
        #a, b: sum(a+b), carry
        dict = { 
            ("0", "0","0") : ("0", "0"),
            ("0", "0","1") : ("1", "0"),
            ("0", "1","0") : ("1", "0"),
            ("0", "1","1") : ("0", "1"),
            ("1", "0","0") : ("1", "0"),
            ("1", "0","1") : ("0", "1"),
            ("1", "1","0") : ("0", "1"),
            ("1", "1","1") : ("1", "1")
            }
        """
        a = "11"
        b = "1"
        Return "100".   
        """
        carry, i, j = '0', len(a)-1, len(b)-1    
        result = ""
        while i>=0 or j>=0:
            d1 = a[i] if i>=0 else '0'
            d2 = b[j] if j>=0 else '0'
            sumd, carry = dict[ (d1, d2, carry) ]
            result = (sumd) + result
            i -= 1
            j -= 1
            
        if carry == '1':
            result = "1"+result
        return result
            
