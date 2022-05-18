class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits)==0: return []
        
        dic = {"2":"abc","3":"def","4":"ghi",
               "5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        """
        res = []
        def backtrack(i,curstr):
            if len(curstr) == len(digits):
                res.append(curstr)
                return 
            for c in dic[digits[i]]:
                backtrack(i+1,curstr+c)
        if digits:
            backtrack(0,"")
        
        return res
        """
        
        output = [""]
        for i in digits:
            tem = []
            for j in dic[i]:
                for o in output:
                    tem.append(o+j)
            output = tem
            
        return output
    
        
        
            
            
        