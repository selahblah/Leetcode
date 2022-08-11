class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        res = float("inf")
        for c in 'balon':
            if c in 'lo':
                res = min(count[c]//2,res)
            else: 
                res = min(count[c],res)
        return res