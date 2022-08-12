class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]
        for i in gain:
            res.append(i+res[-1])
        return max(res)