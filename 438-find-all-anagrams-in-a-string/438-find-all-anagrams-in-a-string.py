class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        count = Counter(p)
        window = Counter(s[:len(p)-1])
        for i in range(len(p)-1,len(s)):
            window[s[i]] = window.get(s[i],0) + 1
            if window == count: res.append(i-len(p)+1)
            window[s[i-len(p)+1]] -= 1
            if window[s[i-len(p)+1]] == 0: del(window[s[i-len(p)+1]])
        return res
            