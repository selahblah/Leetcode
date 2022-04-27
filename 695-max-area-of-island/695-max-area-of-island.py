class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        max_size = 0
        row,col = len(grid), len(grid[0])
        direc=[(-1,0),(0,1),(1,0),(0,-1)]
        
        def dfs(x,y):
            area = 1
            for dx, dy in direc:
                new_x, new_y = x+dx, y+dy
                if 0 <= new_x < row and 0 <= new_y < col and (new_x,new_y) not in visited and grid[new_x][new_y]:
                    visited.add((new_x,new_y))
                    area += dfs(new_x,new_y)
            return area
        
        for x in range(row):
            for y in range(col):
                if grid[x][y] and (x,y) not in visited:
                    visited.add((x,y))
                    max_size = max(dfs(x,y), max_size)
        return max_size        

        
        """
        while i <= len(grid)-1 and j <= len(grid[0])-1:
            if grid[i][j] == grid[i][j+1] == 1:
                a.append((i,j))
                a.append((i,j+1))
                j += 1
            if grid[i][j] == grid[i+1][j] == 1:
                a.append((i,j))
                a.append((i+1,j))
                i += 1
            a_min = min(a_min, len(set(a)))
                    
        return a_min
        """