class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        out=[]
        for i in range(numRows):
            out.append([1])
            for j in range(1,i):
                    out[i].append(out[i-1][j-1] + out[i-1][j])
            if i != 0:
                out[i].append(1)
        return out
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        out=[]
        for i in range(numRows):
            out.append([])
            out[i].append(1)
            for j in range(1,i):
                out[i].append(out[i-1][j-1]+out[i-1][j])
            if i != 0:
                out[i].append(1)
        return out
        """    
        
        
        """
        emp = [[1]]

        if numRows == 1:
            return emp
        else:
            for i in range(numRows+1):
                pas = [0]*i
                for j in range(len(pas)):        
                    if j == 0 or j == len(pas)-1:
                        pas[j] = 1
                    else:
                        pas[j] = emp[i-1][j-1]+emp[i-1][j]
                emp.append(pas)
                
        return emp[1:]
        """