class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        dist = [[[a,b],a**2+b**2] for a,b in points]
        dist.sort(reverse = False, key=lambda x:x[1])
        return [dist[i][0] for i in range(k)]