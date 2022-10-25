class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = Counter(s)
        for ind,ch in enumerate(s):
            if dic[ch] == 1: return ind
        return -1