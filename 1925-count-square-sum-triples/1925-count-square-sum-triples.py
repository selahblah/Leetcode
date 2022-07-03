class Solution:
    def countTriples(self, n: int) -> int:
        res =  0
        for x in range(1,n):
            for y in range(1,n):
                z = x*x + y*y
                zs = int(sqrt(z))
                if zs*zs == z and zs<=n: res += 1
        return res