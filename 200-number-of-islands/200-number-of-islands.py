class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0
        
        def bfs(i,j):
            dq = collections.deque()
            dq.append((i,j))
            visit.add((i,j))
            while dq:
                row,col = dq.popleft()
                udlr = [[0,1],[0,-1],[1,0],[-1,0]]
                for r,c in udlr:
                    i,j = row+r, col+c
                    if (i in range(rows) and
                        j in range(cols) and
                        (i,j) not in visit and 
                        grid[i][j] == "1"):
                        dq.append((i,j))
                        visit.add((i,j))
        
        for i in range(rows):
            for j in range(cols): 
                if grid[i][j] == "1" and (i,j) not in visit:
                    bfs(i,j)
                    islands += 1
                    
        return islands