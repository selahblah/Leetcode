class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dic = Counter(s)
        values = list(dic.values())
        n, keys = values[0], values[1:]
        for key in keys:
            if key != n: return False
        return True
            