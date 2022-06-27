class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False
        
        le1,le2 = len(s1),len(s2)
        cs = Counter(s1)
        i = 0
        while i < le2-le1+2:
            if Counter(s2[i:i+le1]) == cs: return True
            i += 1
        return False