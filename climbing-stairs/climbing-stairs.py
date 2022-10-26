class Solution:
    def climbStairs(self, n: int) -> int:
        one = two = 1
        for i in range(n-1):
            new = one + two
            one = two
            two = new
            
        return two
            