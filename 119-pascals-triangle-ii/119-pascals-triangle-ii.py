class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        out = []
        for i in range(rowIndex+1):
            out.append([])
            out[i].append(1)
            for j in range(1,i):
                out[i].append(out[i-1][j-1]+out[i-1][j])
            if i != 0:
                out[i].append(1)
                
        return out[rowIndex]
        
        
        """
        emp = [[1]]

        if rowIndex == 0:
            return emp[0]
        else:
            for i in range(1, rowIndex+2):
                pas = [0]*i
                for j in range(len(pas)):        
                    if j == 0 or j == len(pas)-1:
                        pas[j] = 1
                    else:
                        pas[j] = emp[i-1][j-1]+emp[i-1][j]
                emp.append(pas)

        emp = emp[1:]
        
        return emp[rowIndex]
        """