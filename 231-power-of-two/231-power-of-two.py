class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        return n>0 and n&(n-1) == 0 
    
        """
        if n <= 0:
            return False
        while n %2 ==0:
            n = n/2
        return n == 1
        """
        
        """
        if n == 1:
            print(1, n)
            return True
        elif (n%2) == 1:
            print(11, n%2)
            return False
        else:
            print(111, n//2)
            self.isPowerOfTwo(n//2)
        """

            