class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        N = len(arr)
        total = 0
        
        for k in range(1,N+1,2):
            for t in range(N-k+1):
                total += sum(arr[t:t+k])
        return total
        
        """
        res = sum(arr)
        tem = 3
        while tem <= len(arr):
            for start in range(len(arr)-tem+1)[::-1]:
                li = []
                while len(li)<tem:
                    li.append(arr[start])
                    start += 1
                res += sum(li)
            tem += 2
        
        return res
        """