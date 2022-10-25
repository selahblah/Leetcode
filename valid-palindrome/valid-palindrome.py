class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = inv = ""
        for c in s:
            if c.isalpha() or c.isnumeric(): s2 += c.lower()
        for c in s2[::-1]:
            inv += c
        return inv == s2
        
        