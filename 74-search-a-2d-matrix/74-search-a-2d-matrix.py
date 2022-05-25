class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i,j = len(matrix)-1, 0
        
        while i > -1 and j < len(matrix[0]):
            while i>-1 and matrix[i][j] > target: i -= 1
            while j<len(matrix[0]) and matrix[i][j] < target: j += 1
            return True if i > -1 and j < len(matrix[0]) and matrix[i][j] == target else False