"""
class Solution {
public:
    int minCut(string s) {
        int n = s.size();
        vector<int> cut(n+1, 0);  // number of cuts for the first k characters
        for (int i = 0; i <= n; i++) cut[i] = i-1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; i-j >= 0 && i+j < n && s[i-j]==s[i+j] ; j++) // odd length palindrome
                cut[i+j+1] = min(cut[i+j+1],1+cut[i-j]);

            for (int j = 1; i-j+1 >= 0 && i+j < n && s[i-j+1] == s[i+j]; j++) // even length palindrome
                cut[i+j+1] = min(cut[i+j+1],1+cut[i-j+1]);
        }
        return cut[n];
    }
};
"""

#O(n) space comliexity
"""
有个更好的算法，只需要O(n)空间：https://oj.leetcode.com/discuss/9476/solution-does-not-need-table-palindrome-right-uses-only-space.
其实这题关键在于怎样判断palindrome，而判断的方法有两种：一种是递归构造，另一种是枚举所有中心点然后向两方向扩散。我发现绝大多数解法都是基于第一种的，但其实如果基于第二种的话能够省去那个O(n^2)的空间，这也就是链接中方法的思想。﻿
"""
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        d = [ i-1 for i in range(length+1)]
        #for i in range(length):
        #    if s[:i+1] == s[i::-1]:
        #        d[i] = 0
                
        # d[i] = min ( i,  min( d[j-1]+1 [if j+1---i is palindrome ] )  )
        for i in range(length):
            #odd length palindrome
            for j in range(i+1):
                if i+j< length and s[i-j] == s[i+j]:
                    d[i+j+1] = min(d[i+j+1], d[i-j]+1)
            #even length palindrom
            for j in range(1, i+2):
                if i+j < length and s[i-j+1] == s[i+j]:
                    d[i+j+1] = min(d[i+j+1], d[i-j+1]+1)
                    
        return d[-1]
