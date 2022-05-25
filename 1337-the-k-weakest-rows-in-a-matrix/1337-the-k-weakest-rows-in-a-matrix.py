class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        has = []
        for i in range(len(mat)):
            j = 0
            while j<len(mat[0]) and mat[i][j] == 1: j+=1 
            has.append([i,j])
        has = sorted(has,key=lambda x:x[1])
        return [has[i][0] for i in range(k)]
        