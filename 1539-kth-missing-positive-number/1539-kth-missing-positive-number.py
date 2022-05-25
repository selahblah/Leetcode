class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        has = [i for i in range(1,arr[-1]+k+1)]
        
        for i in has:
            if i not in arr:
                k -= 1
            if k == 0: return i