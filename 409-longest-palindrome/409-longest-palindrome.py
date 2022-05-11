class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        
        if len(s) ==1: return 1
        
        S = Counter(s)
        value = list(S.values())
        
        res = 0
        odd_li = []
        for n in value:
            if n % 2 == 0:
                res += n
            else:
                odd_li.append(n)
                
        if not odd_li: return res
        elif len(odd_li) == 1: res = res + odd_li[0]
        else: res = res + sum(odd_li) - len(odd_li) + 1
        return res