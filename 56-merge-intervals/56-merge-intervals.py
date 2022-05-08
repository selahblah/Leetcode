class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        res = [intervals[0]]
        
        for li in intervals[1:]:
            lastend = res[-1][1]
            start = li[0]
            end = li[1]
            if lastend >= start:
                res[-1][1] = max(end,lastend)
            else:
                res.append(li)
                
        return res