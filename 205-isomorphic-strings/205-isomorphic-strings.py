class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sdic,tdic=defaultdict(list),defaultdict(list)
        for i in range(len(s)):
            sdic[s[i]].append(i)
        for i in range(len(t)):
            tdic[t[i]].append(i)
        
        return list(sdic.values()) == list(tdic.values())