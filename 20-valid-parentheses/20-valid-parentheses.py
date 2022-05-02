class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        ls = list(s)
        stack = []
        
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif len(stack) != 0:
                if (i == ')' and stack[-1] == '(') or (i == ']' and stack[-1] == '[') or (i == '}' and stack[-1] == '{'):
                    stack.pop()
                else:
                    return False
            else:
                return False
            
        if not stack:
            return True

            
            
        