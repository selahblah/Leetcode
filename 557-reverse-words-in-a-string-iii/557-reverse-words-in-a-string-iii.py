class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        res = ""
        for word in s:
            for i in word[::-1]:
                res += i
            res += " "
        return res[:-1]