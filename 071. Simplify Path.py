"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_list = path.split("/")
        stack = []
        for token in path_list:
            if token == "" or token == ".":
                continue
            elif token == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(token)
        return "/"+ "/".join(stack)
                
