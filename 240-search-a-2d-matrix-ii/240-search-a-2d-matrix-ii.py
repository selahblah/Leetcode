class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for li in matrix:
            if target >= min(li) and target <= max(li):
                if target in li:
                    return True
                
        return False