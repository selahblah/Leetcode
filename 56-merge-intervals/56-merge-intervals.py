class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]
        
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            
            if start <= lastEnd:
                output[-1][1] = max(lastEnd,end)
            else:
                output.append([start,end])
        
        return output
        
        """
        res = []
        i = 0
        while i <= len(intervals)-2:
            if intervals[i][1] >= intervals[i+1][0]:
                res.append([intervals[i][0],intervals[i+1][1]])
                i += 2
            else:
                res.append(intervals[i])
                i += 1
            
        return res
        """
            