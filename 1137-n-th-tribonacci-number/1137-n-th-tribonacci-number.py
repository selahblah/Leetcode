class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0: return 0
        elif n==1: return 1
        elif n==2: return 1
        """
        has = [0,1,1]
        for i in range(n-2):
            tem = has[i]+has[i+1]+has[i+2]
            has.append(tem)
        """
        has = deque([0,1,1])    
        while n-2 > 0:
            has.append(sum(has))
            has.popleft()
            n -= 1
        
        return has[-1]