class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i,l = 0,len(p)
        dic,window = Counter(p),Counter(s[i:i+l])
        res = []
        while i < len(s)-l+1:
            if window == dic: res.append(i)
            if window[s[i]] == 1: del window[s[i]]
            else: window[s[i]] -= 1
            i += 1
            if i+l-1 < len(s): window[s[i+l-1]] = window.get(s[i+l-1],0) + 1
            
        return res
            