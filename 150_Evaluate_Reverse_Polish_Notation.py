"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for n in tokens:
            if n == "+":
                num = stack.pop() + stack.pop()
                stack.append(num)
            elif n == "-":
                n1 = stack.pop()
                n2 = stack.pop()
                num = n2 - n1
                stack.append(num)
            elif n == "*":
                num = stack.pop() * stack.pop()
                stack.append(num)
            elif n == "/":
                n1 = stack.pop()
                n2 = stack.pop()
                num =int( float(n2) / n1)
                stack.append(num)
            else:
                stack.append(int(n))
        return stack[-1]        
