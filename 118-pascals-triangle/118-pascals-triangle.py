class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1,numRows):
            tem = [1]
            j = 0
            while len(tem) < i:
                tem.append(res[-1][j]+res[-1][j+1])
                j += 1
            tem.append(1)
            res.append(tem)
        return res