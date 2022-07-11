class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        r,c = len(grid)-1,0
        res = 0 
        while r > -1 and c < len(grid[0]):
            while r > -1 and grid[r][c] < 0:
                res += len(grid[0])-c
                r -= 1
            while c < len(grid[0]) and grid[r][c] >= 0:
                c += 1
        return res
        
    
        """
        res = 0
        for li in grid[::-1]:
            for i in range(len(li)):
                if li[i] < 0:
                    res += len(li) - i
                    break
        return res
        """     