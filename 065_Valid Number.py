"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
"""

import re
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.derterministic_finite_automation(s)
        return self.regular_exp(s)
        return self.simple(s)
    
    #"\d*\.?\d*": this will match .
    #"\d+\.?\d*|\d*\.?\d+" will match any 21221, 1.200, 1., .211
    def regular_exp(self, s):
        pattern = "^[\ ]*[+-]?(\d+\.?\d*|\d*\.?\d+)(e[+-]?\d+)?[\ ]*$"
        pattern = "^[\ ]*(\+|\-)?([0-9]+|[0-9]+\.[0-9]*|[0-9]*\.[0-9]+)(e(\+|\-)?[0-9]+)?[\ ]*$"
        reg = re.compile(pattern)
        return bool(reg.match(s))
        
    def simple(self, s):
        try:
            float(s)
            return True
        except:
            return False
    
    def derterministic_finite_automation(self, s):
        state = {}
        #sucessful state: 3,5,8,9
        state[1]= {"space":1, "sign":2, "digit":3, ".":4}  #state 1
        state[2]= { "digit":3, ".":4 }
        state[3]= {"space":9, "digit":3, "e":6, ".":5}
        state[4]= {"digit":5}
        state[5]= {"digit":5, "e":6, "space": 9}
        state[6]= {"sign":7, "digit":8}
        state[7]= {"digit":8}
        state[8]= {"digit":8, "space":9}
        state[9]= {"space":9}
        
        current_state = 1
        for ch in s:
            c = "other"
            if ch in "0123456789":
                c = "digit"
            elif ch == " ":
                c = "space"
            elif ch in "+-":
                c = "sign"
            elif ch == ".":
                c = "."
            elif ch == "e":
                c = "e"
            
            print current_state, ch   
            if c not in state[current_state].keys():
                return False
            current_state = state[current_state][c]
        
        if current_state in [3, 5, 8, 9]:
            return True
            
        return False
        
