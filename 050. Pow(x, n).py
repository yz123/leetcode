#五种不同选择
#https://discuss.leetcode.com/topic/21837/5-different-choices-when-talk-with-interviewers
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        return self.binary(x, n)
        
        import math
        return math.pow(x,n)
    
    def binary(self, x, n):
        if n < 0: return 1.0/self.binary(x, -n)
        if n == 0: return 1
        
        sqrt_x = self.binary(x, n/2)
        
        if n%2 ==0:
            return sqrt_x*sqrt_x
        else:
            return x*sqrt_x*sqrt_x


"""
#bit operation
n = k0*2^0 + k1*2^1 + ... +k31*2^31
x^n = x^(k0*2^0 + k1*2^1 + ... +k31*2^31) = x^(k0*2^0) * x^{k1*2^1} * ... * x^{k31*2^31}
class Solution {
public:
    double pow(double x, int n) {
    	if(n<0){
    		x = 1.0/x;
    		n = -n;
    	}
    	int unsigned m = n;
        double tbl[32] = {0};
        double result = 1;
        tbl[0] = x;
        for(int i=1;i<32;i++){
            tbl[i] = tbl[i-1]*tbl[i-1];
        }
        for(int i=0;i<32;i++){
            if( m & (0x1<<i) )
            result *= tbl[i];
        }
        return result;
    }
};
In bit format and for a unsigned number, the number is represented as k0*2^0 + k1*2^1 + ... +k31*2^31. Therefore, once we know the pow(x,2^0), pow(x,2^1), ..., pow(x,2^31), we can get pow(x,n). And pow(x,2^m) can be constructed easily as pow(x,2^m) = pow(x,2^(m-1)*pow(x,2^(m-1).
"""
        
