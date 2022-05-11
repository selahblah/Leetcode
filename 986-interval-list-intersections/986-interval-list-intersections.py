class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        a,b = 0,0
        N,M = len(firstList),len(secondList)
        
        res = []
        while (a<N and b<M):
            start = max(firstList[a][0],secondList[b][0])
            end = min(firstList[a][1],secondList[b][1])
            
            if start <= end:
                res.append([start,end])
            
            if firstList[a][1] < secondList[b][1]:
                a += 1
            else:
                b += 1
        return res
                
        
        
        """
        if not (firstList and secondList): return []
        left1, left2 = 0, 0
        
        res = [[max(firstList[left1][0],secondList[left2][0]), 
                min(firstList[left1][1],secondList[left2][1])]]
        prev_end = max(firstList[left1][1],secondList[left2][1])
        left1, left2 = 1, 1
        
        while left1 < len(firstList) and left2 < len(secondList):
            start_min = min(firstList[left1][0],secondList[left2][0])
            start_max = max(firstList[left1][0],secondList[left2][0])
            end_min = min(firstList[left1][1],secondList[left2][1])
            
            if prev_end > start_min:
                res[-1][0] = max(start_min, res[-1][0])
                res[-1][-1] = min(prev_end,end_min)
            elif prev_end == start_min:
                res.append([start_min,prev_end])
            if end_min >= start_max: res.append([start_max,end_min])
            
            prev_end = max(firstList[left1][1],secondList[left2][1])
            left1 += 1
            left2 += 1
        
        return res
        """