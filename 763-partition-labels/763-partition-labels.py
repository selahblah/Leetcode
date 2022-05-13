class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c:i for i, c in enumerate(s)}
        
        output, maxi, size = [], -1, 1
        for i, c in enumerate(s):
            maxi = max(maxi,last[c])
            if i == maxi:
                output.append(size)
                size =1
            else: size += 1
        
        return output
                    
            
        