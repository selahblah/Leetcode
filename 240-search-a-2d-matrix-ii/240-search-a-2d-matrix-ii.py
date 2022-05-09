class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for li in matrix:
            if max(li) < target:
                continue
            if target in li:
                return True
                
        return False