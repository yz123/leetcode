"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
         
        dict = {}
        start = 0
        dp = 0
        max_l = 0
        
        for i, ch in enumerate(s):
            if ( ch not in dict) or (dict[ch]<start):
                dict[ch] = i
                dp = dp + 1
            else:
                max_l = max(max_l, dp)
                start = dict[ch]+1
                dp = i - start + 1
                dict[ch] = i
                
        return max(max_l, dp)


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        isIn = {}
        start = 0
        length = 0
        for cur in range(len(s)):
            a = s[cur]
            #a is in the substring without repeating characters:
            if ( a not in isIn ) or (isIn[a]<start):
                isIn[a] = cur
                length += 1
            else:
            # a has been repeated:
                if length > longest:
                    longest = length
                start = isIn[a]+1
                isIn[a] = cur
                length = cur - start +1
        if length > longest:
            longest = length
        return longest
