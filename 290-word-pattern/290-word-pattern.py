class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s2 = s.split()
        pattern = list(pattern)
        if len(pattern) != len(s2): return False
        if len(set(pattern)) != len(set(s2)): return False
        
        dic=dict(zip(pattern,s2))
        
        for i in range(len(pattern)):
            if dic[pattern[i]] != s2[i]:
                return False
        return True
                