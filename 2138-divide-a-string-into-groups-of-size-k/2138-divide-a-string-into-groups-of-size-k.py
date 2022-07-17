class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = [""]
        for c in s:
            if len(res[-1])<k:
                res[-1] += c
            else:
                res.append(c)
        
        while len(res[-1])<k:
            res[-1] += fill
        return res