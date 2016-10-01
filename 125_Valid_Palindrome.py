"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        length = len(s)
        
        begin = 0
        end = length -1
        while begin < end:
            while begin < length and not s[begin].isalnum():
                begin += 1
            while end >=0 and not s[end].isalnum():
                end -= 1
    
            if begin < end and s[begin].lower() != s[end].lower():
                return False
    
            begin += 1
            end -= 1
        
        return True
