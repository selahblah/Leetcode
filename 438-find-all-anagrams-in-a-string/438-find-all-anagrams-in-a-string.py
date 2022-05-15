class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        i, n = 0, len(p)
        countW = Counter(p)
        countS = Counter(s[:n-1])
        res = []
        
        
        while i <= len(s)-n:
            countS[s[i+n-1]] += 1
            if countS == countW: res.append(i)
            countS[s[i]] -= 1
            if countS[s[i]] ==0: countS.pop(s[i])
            i += 1
            
        return res
            
        