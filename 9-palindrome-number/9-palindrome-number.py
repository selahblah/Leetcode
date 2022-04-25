class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        sx1 = list(str(x))
        sx2 = list(str(x)[:])
        sx1.reverse()
        
        if sx1 == sx2:
            return True
        else:
            return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        A=1
        str1=str(x)
        num = []
        for i in range(0, len(str1), A):
            num.append(str(str1[i : i + A]))
        
        rev_num = num[::-1]

        if num == rev_num:
             return True
        else:
            return False
        """