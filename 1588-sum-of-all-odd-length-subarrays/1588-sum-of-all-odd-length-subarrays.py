class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
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