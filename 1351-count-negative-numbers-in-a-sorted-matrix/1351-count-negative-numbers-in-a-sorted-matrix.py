class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        lr = len(grid[0])
        r,c,res = len(grid)-1,0,0
        while r>-1 and c<lr:
            if grid[r][c]<0: res += lr-c
            else: 
                while c<lr and grid[r][c]>=0: c+=1
                if c<lr and grid[r][c]<0: res += lr-c
            r -= 1
        return res