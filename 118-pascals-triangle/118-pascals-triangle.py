class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        emp = [[1]]

        if numRows == 1:
            return emp
        else:
            for i in range(1, numRows+1):
                pas = [0]*i
                for j in range(len(pas)):        
                    if j == 0 or j == len(pas)-1:
                        pas[j] = 1
                    else:
                        pas[j] = emp[i-1][j-1]+emp[i-1][j]
                emp.append(pas)
                
        return emp[1:]