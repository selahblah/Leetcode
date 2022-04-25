class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        from collections import Counter 
        
        count = Counter(s)
        value_list = list(count.values())
        key_list = list(count.keys())
        index = 0
        
        for i in s:
            if value_list[key_list.index(i)] == 1:
                return index
            else:
                index += 1
                
        return -1
        
        
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
    """
        