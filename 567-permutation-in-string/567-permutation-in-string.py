class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False
        
        le1,le2 = len(s1),len(s2)
        window = Counter(s2[0:le1-1])
        cs = Counter(s1)
        for i in range(le2-le1+1):
            window[s2[i+le1-1]] += 1
            if window == cs: return True
            window[s2[i]] -= 1
        return False