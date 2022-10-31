class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=itemgetter(0))
        res = []
        i = 0
        while i < len(intervals):
            res.append(intervals[i])
            while i+1 < len(intervals) and res[-1][1] >= intervals[i+1][0]: 
                res[-1][1] = max(res[-1][1],intervals[i+1][1])
                i += 1
            i += 1
        return res