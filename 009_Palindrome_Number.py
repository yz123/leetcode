"""
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
"""

#idea: 
#compare the left and right.
#if left==right, then x = x% left; x = x/ right, to remove the left and right number

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
            
        l_index = 1
        while x/l_index >= 10:
            l_index *= 10
        
        while x:
            left = x/l_index
            right = x%10
            if left != right:
                return False
            x %= l_index
            x /= 10
            l_index /=100
        return True
