class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left, right = 0, len(matrix[0])-1
        top, bottom = 0, len(matrix)-1
        i = 0
        
        while left <= right and top <= bottom:
            if matrix[bottom][left] == target:
                return True
            if matrix[bottom][left] > target:
                bottom -= 1
            else:
                left += 1
            
        return False

        """
        for li in matrix:
            if target <= li[-1]:
                if target in li:
                    return True
            if target <= li[0]:
                break
        return False
        """