class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        res = float("inf")
        out = 0
        for n in range(len(points)):
            i,j = points[n][0], points[n][1]
            if i != x and j != y: continue
            else: 
                if abs(i-x) + abs(j-y) < res:
                    res = abs(i-x) + abs(j-y)
                    out = n
        
        return -1 if res == float("inf") else out