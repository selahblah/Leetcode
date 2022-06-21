class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        return self.sol(s) == self.sol(t)
    
    def sol(self,x):
        i = 0
        while i < len(x):
            if x[0] == "#": x = x[1:]
            elif i>0 and i<len(x)-1 and x[i] == "#": 
                x=x[:i-1]+x[i+1:]
                i -= 1
            elif i>0 and x[i] == "#": 
                x=x[:i-1]
                i += 1
            else: i += 1
        return x