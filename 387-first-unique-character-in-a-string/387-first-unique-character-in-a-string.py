class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ls = list(s)
        emp = []
        
        if len(s) == 1:
            return 0

        for i in range(len(ls)-1):
            if ls[i] in ls[i+1:]:
                emp.append(ls[i])
            else:
                if ls[i] in emp:
                    pass
                else:
                    return(i)
        
        if not ls[-1] in emp:
            return len(ls)-1
        else:
            return -1
    
        