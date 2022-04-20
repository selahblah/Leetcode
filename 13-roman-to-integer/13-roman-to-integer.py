class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        result = 0
        
        for i in range(len(s)-1):
            if roman[s[i]] >= roman[s[i+1]]:
                result = result + roman[s[i]] 
            else:
                result = result - roman[s[i]]

        result = result + roman[s[len(s)-1]]
        return result