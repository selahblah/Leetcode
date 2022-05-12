class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
    
        res = []
        M, N = len(s), len(p)
        counterS = Counter(p)
        counterW = Counter(s[:N-1])
        
        for i in range(N-1,M):
            indx = i - (N-1)
            counterW[s[i]] += 1
            
            if counterW == counterS:
                res.append(indx)
            counterW[s[indx]] -= 1
            if counterW[s[indx]] == 0:
                counterW.pop(s[indx])
        
        return res
            
        
        """
        res = []
        s, p = list(s), list(p)
        
        for i in range(len(s)-len(p)+1):
            j = 0
            tem = s
            tem = tem[i:i+len(p)]
            if s[i] not in p:
                continue
            while j < len(p):
                if p[j] in tem:
                    tem.remove(p[j])
                    j += 1
                else: break
                if not tem: res.append(i)
        return res
        """    
                
                