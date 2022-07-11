class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(mat)*len(mat[0]) != r*c: return mat
        res = []
        tem = deque()
        for li in mat:
            for i in li: tem.append(i)
                
        C = len(tem)//r
        for row in range(r):
            li = []
            while len(li)<C:
                li.append(tem.popleft())
            res.append(li)
        return res