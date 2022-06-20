class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0 
        elif n == 1: return 1
        
        tem1, tem2, res = 0, 1, 0
        for i in range(n-1):
            res = tem2 + tem1
            tem1 = tem2
            tem2 = res
        return res
            