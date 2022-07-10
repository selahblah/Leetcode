class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for li in grid[::-1]:
            for i in range(len(li)):
                if li[i] < 0:
                    res += len(li) - i
                    break
        return res
                
                