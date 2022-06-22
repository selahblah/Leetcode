class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        start_r, end_r, start_c, end_c = 0, len(matrix), 0, len(matrix[0])
        res = []
        while start_r<end_r and start_c<end_c:
            # left to right
            if start_r<end_r: res.extend([matrix[start_r][i] for i in range(start_c,end_c)])
            start_r += 1
            
            # up to bottom
            if start_c<end_c: res.extend([matrix[i][end_c-1] for i in range(start_r,end_r)]) 
            end_c -= 1
            
            # right to left
            if start_r<end_r: res.extend([matrix[end_r-1][i] for i in range(end_c-1,start_c-1,-1)])
            end_r -= 1
            
            # bottom to up
            if start_c<end_c: res.extend([matrix[i][start_c] for i in range(end_r-1,start_r-1,-1)])
            start_c += 1
        
        return res
                