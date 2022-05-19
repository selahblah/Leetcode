class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row,col = len(grid), len(grid[0])
        q = deque()
        direc = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        visit = set()
        count = 0
        
        if grid[0][0] == 0:
            q.append((count+1,(0,0)))
            visit.add((0,0))
        
        while q:
            count, tem = q.popleft()
            i,j = tem[0], tem[1]
            if (i,j) == (row-1, col-1):
                return count
            for r, c in direc:
                cur_r, cur_c = i+r, j+c
                if cur_r in range(row) and cur_c in range(col) and grid[cur_r][cur_c] == 0 and (cur_r,cur_c) not in visit:
                    q.append((count+1,(cur_r,cur_c)))
                    visit.add((cur_r,cur_c))
        return -1
                    
                