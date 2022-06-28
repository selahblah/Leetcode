class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        res = 0
        tem = intervals[0]
        for i,j in intervals[1:]:
            if tem[0] <= i < tem[1]: 
                res += 1
                tem[1] = min(tem[1],j)
            else: tem = [i,j]
        return res