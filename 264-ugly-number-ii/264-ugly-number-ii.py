class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        res = [1]
        two = three = five = 0
        while len(res) < n:
            while res[two]*2 <= res[-1]: two += 1
            while res[three]*3 <= res[-1]: three += 1
            while res[five]*5 <= res[-1]: five += 1
            res.append(min(res[two]*2,res[three]*3,res[five]*5))
        
        return res[-1]
        
        """
        if n == 1: return 1
        
        i,res = 0, 2
        while i < n:
            for p in [2,3,5]:
                while res%p == 0:
                    res = res//p
            if res == 1: i += 1
            if i == n: return res
            else: res += 1
        """
        
    