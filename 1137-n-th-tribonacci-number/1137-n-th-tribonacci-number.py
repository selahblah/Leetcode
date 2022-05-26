class Solution:
    def tribonacci(self, n: int) -> int:
        t0,t1,t2 = 0,1,1
        if n==0: return t0
        elif n==1: return t1
        elif n==2: return t2
        
        for i in range(n-2):
            tem = t0+t1+t2
            t0 = t1
            t1 = t2
            t2 = tem
        
        return t2
        
        """
        has = deque([0,1,1])    
        while n-2 > 0:
            has.append(sum(has))
            has.popleft()
            n -= 1
        
        return has[-1]
        """
        """
        has = [0,1,1]
        for i in range(n-2):
            tem = has[i]+has[i+1]+has[i+2]
            has.append(tem)
        """