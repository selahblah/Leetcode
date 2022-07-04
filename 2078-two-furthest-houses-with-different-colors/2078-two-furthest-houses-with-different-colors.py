class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)-1
        for i in range(n):
            if colors[i]!=colors[n] or colors[0] != colors[n-i]: 
                return n-i
        return 0