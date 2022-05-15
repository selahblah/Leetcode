class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        
        res = []
        a,b = 0, 0
        A,B = len(firstList), len(secondList)
        
        while a<A and b<B:
            start = max(firstList[a][0],secondList[b][0])
            end = min(firstList[a][1],secondList[b][1])
            
            if start <= end: res.append([start,end])
                
            if firstList[a][1] < secondList[b][1]:
                a += 1
            else: b += 1
            
        return res