class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        N,M = len(mat[0]), len(mat)
        T = r*c
        if N*M != T: return mat
        
        output = [[0 for _ in range(c)] for _ in range(r)]
        k = 0
        for i in range(M):
            for j in range(N):
                output[k//c][k%c] = mat[i][j]
                k += 1
                
        return output
        
        """
        if len(mat) == r: return mat
        tem = has = res = [] 
        col = len(mat)*len(mat[0])//r
        
        for i in mat:
            has += i
        for i in has:
            if len(tem) == col:
                res.append(tem)
                tem = []
            tem.append(i)
        return res
        """