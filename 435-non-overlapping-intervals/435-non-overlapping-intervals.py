class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals)
        count = 0
        pre_end = intervals[0][1]
        
        for start, end in intervals[1:]:
            if start < pre_end: 
                count += 1
                pre_end = min(end, pre_end)
            else: pre_end = end
        return count
                
                

            
        
        while i < len(intervals)-1:
            if intervals[i][1] > intervals[i+1][0]:
                res += 1
                i += 2
            else: i += 1
        
        if intervals[-2][1] > intervals[-1][0]:
            res += 1
        
        return res
                