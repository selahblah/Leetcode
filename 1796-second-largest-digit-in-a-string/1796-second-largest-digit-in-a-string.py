class Solution:
    def secondHighest(self, s: str) -> int:
        res = []
        for i in s:
            if i.isdigit(): res.append(i)
        res = sorted(set(res))
        return res[-2] if len(res)>1 else -1