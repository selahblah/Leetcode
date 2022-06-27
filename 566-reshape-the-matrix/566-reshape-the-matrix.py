class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(mat)*len(mat[0]) != r*c: return mat
        new_c = len(mat)*len(mat[0])//r
        i,res = 0,[]
        
        mat = [x for xs in mat for x in xs]
        
        while i < len(mat):
            tem = []
            while i < len(mat) and len(tem) < new_c:
                tem.append(mat[i])
                i += 1
            res.append(tem)
        return res
            