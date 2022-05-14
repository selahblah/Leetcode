class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        
        res = [intervals[0]]
        for i,j in intervals[1:]:
            if res[-1][1] >= i:
                res[-1][1] = max(j,res[-1][1])
            else: res.append([i,j])

        return res