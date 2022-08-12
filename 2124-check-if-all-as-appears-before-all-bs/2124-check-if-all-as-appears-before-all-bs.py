class Solution:
    def checkString(self, s: str) -> bool:
        b = False
        for x in s:
            if x == 'b':
                b = True
            else:
                if b: return False
        return True
                
        
        """
        num = float("inf")
        for i in range(len(s)):
            if s[i] == 'b':
                num = i
                break
        if num == float("inf"): return True
        
        for j in range(num,len(s)):
            if s[j] == 'a': return False
        return True
        """
            