class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x<=arr[0]: return arr[:k]
        elif x>=arr[-1]: return arr[-k:]
        res = [[abs(i-x),i-x] for i in arr]
        res.sort()
        return sorted([j+x for i,j in res[:k]])