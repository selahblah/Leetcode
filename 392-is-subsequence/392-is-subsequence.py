class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        if not s: return True
        for i in t[::-1]:
            if i == s[-1]: s.pop()
            if not s: return True
        return False