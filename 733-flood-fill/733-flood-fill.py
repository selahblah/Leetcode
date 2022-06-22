class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        tem = image[sr][sc]
        if tem == color: return image
        
        r,c = len(image), len(image[0])
        visit = []
        direction = [(-1,0),(0,1),(0,0),(1,0),(0,-1)]
        
        def dfs(sr,sc):
            for i,j in direction:
                new_sr, new_sc = sr + i, sc + j
                if -1<new_sr<r and -1<new_sc<c and (new_sr,new_sc) not in visit and image[new_sr][new_sc] == tem:
                    visit.append((new_sr,new_sc))
                    image[new_sr][new_sc] = color
                    dfs(new_sr,new_sc)
            return image
        
        return dfs(sr,sc)
        
        """
        tem = image[sr][sc]
        image[sr][sc] = color
        visit = []
        direction = [[-1,-1],[-1,1],[1,1],[1,-1]]
        while -1<sr<len(image) and -1<sc<len(image[0]):
            for i,j in direction:
                sr += i
                sc += j
                if -1<sr<len(image) and -1<sc<len(image[0]) and [sr,sc] not in visit and image[sr][sc] == tem:
                    visit.append([sr,sc])
                    image[sr][sc] = color
        return image
        """