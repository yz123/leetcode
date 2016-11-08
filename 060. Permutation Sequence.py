"""
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        return self.recursion_method(n,k)
    
    #idea: f(1) = 1, f(2) = 2, f(3) = 6, f(4) = 24
    #example: n = 3, k =5
    #123 132;  213, 231; 312 321
    #从k-1开始， k-1/f(2) (f(n-1)) ＝ 2 为第几组 （第二组， 312, 321）; k-1 % f(2) =0 (第0个： 312） （递归为n=2时从［1，2］中取第0个）
    def recursion_method(self, n, k):
        #get factorial
        factorial = [1]*(n+1)
        for i in xrange(2, n+1):
            factorial[i] = factorial[i-1]*i
        
        self.res = ""
        path = []
        num_set = [ str(i) for i in xrange(1,n+1) ]
        
        #k start with 0
        self.get_per(num_set, n, k-1, factorial, path)
        return self.res
    
    def get_per(self, num_set, n, k, factorial, path):
        if len(num_set)==0:
            self.res = "".join(path)
            return
            
        index = k/factorial[n-1]    
        cur_k = k%factorial[n-1]
        #print index, cur_k, n-1, factorial[n-1]
        #print "".join(path)
        num = num_set.pop(index)
        self.get_per(num_set, n-1, cur_k, factorial, path+[num])
        
