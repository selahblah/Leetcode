class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        window = Counter(s[:k-1])
        res = 0
        for i in range(k-1,len(s)):
            window[s[i]] = window.get(s[i],0) + 1
            res = max(res, window['a']+window['e']+window['i']+window['o']+window['u'])
            if res == k: return res
            window[s[i-k+1]] -= 1
        return res
        