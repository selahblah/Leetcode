class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        k = 1
        for i in range(len(arr)):
            k = 0
            while i+k < len(arr):
                res += sum(arr[i:i+k+1])
                k += 2
        return res