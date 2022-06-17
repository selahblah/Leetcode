class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr)<3: return False
        i = 0
        while i < len(arr)-2:
            if arr[i]%2 == 1 and arr[i+1]%2 == 1 and arr[i+2]%2 == 1: return True
            elif arr[i+1]%2 == 1: i += 1
            elif arr[i+2]%2 == 1: i += 2
            else: i += 3
        return False