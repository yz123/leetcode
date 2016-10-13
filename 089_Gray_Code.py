"""
he gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
"""

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        #return self.dfs(n)
        return self.intelligent(n)
    
    def intelligent(self, n):
        if n==0: return [0]
        if n==1: return [0, 1]
        else:
            f_pre = self.intelligent(n-1)
            res = f_pre
            #print 1<< (n-1)
            res += [ ( (1<<(n-1)) + a) for a in reversed(f_pre)]
        return res
      
    #using backtracking    
    def dfs(self, n):    
        if n == 0: return [0]
        
        self.res = []
        self.isIn = {}
        
        root = "0"* n
        self.isIn[int(root,2)]=True
        self.res.append(int(root,2))
        print root
        self.backtracking(root, pow(2,n))
        
        return self.res
    
    def backtracking(self, root, total):
        if len(self.res)==total:
            return
        for i in xrange(len(root)):
            char = "0"
            if root[i]=="0":
                char = "1"
            new = root[:i]+ char + root[i+1:]
            num = int(new, 2)
            if num not in self.isIn:
                self.isIn[num]=True
                self.res.append(num)
                print new
                self.backtracking(new, total)
                break
        
