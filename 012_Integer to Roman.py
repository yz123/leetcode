"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution:
    # @return a string
    def intToRoman(self, num):
        bases=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        map={1000:"M", 900:"CM", 500:"D",400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
        i=0
        r_num=""
        while num>0:
            if num-bases[i]>=0:
                r_num=r_num+map[bases[i]]
                num=num-bases[i]
            else:
                i=i+1
        return r_num
