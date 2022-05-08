class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        l, r = 0, len(matrix)-1
        
        while l < r:
            for i in range(r-l):
                top, bottom = l, r

                topleft = matrix[top][l+i]

                #bottomleft -> topleft
                matrix[top][l+i] = matrix[bottom-i][l]
                
                #bottomright -> bottomleft
                matrix[bottom-i][l] = matrix[bottom][r-i]
                
                #topright -> bottomright
                matrix[bottom][r-i] = matrix[top+i][r]
                
                #topleft -> topright
                matrix[top+i][r] = topleft
                
            l += 1
            r -= 1
        
        """
        res = []
        i = 0
        while i < len(matrix):
            tem = []
            for num in matrix[::-1]:
                tem.append(num[i])
            res.append(tem)
            i += 1 
        
        return res
        """