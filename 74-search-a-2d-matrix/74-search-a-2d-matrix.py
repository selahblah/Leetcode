class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for li in matrix:
            if target <= li[-1]:
                if target in li:
                    return True
            if target <= li[0]:
                break
        return False
    
        """
        for ma in matrix:
            for i in ma:
                if i == target:
                    return True
                elif i > target:
                    return False
        """