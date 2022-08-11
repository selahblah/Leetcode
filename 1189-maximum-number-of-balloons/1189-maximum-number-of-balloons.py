class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        w = ['b','a','l','o','n']
        res = float("inf")
        for c in w:
            if c == 'l' or c == 'o':
                count[c] = count[c]//2
            else: count[c] = count.get(c,0)
            res = min(count[c],res)
        return res