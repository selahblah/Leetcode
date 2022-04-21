class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
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