class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res = []
        def rec(start,end,stack,figure):
            if start == end == 0: 
                res.append(figure)
                return
            if start >0:
                rec(start-1,end,stack+1,figure+"(")
            if end > 0 and stack >0:
                rec(start,end-1,stack-1,figure+")")
        
        rec(n,n,0,"")
        
        return res
        