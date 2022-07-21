class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = 0
        for i in range(len(number)):
            if number[i] == digit:
                tem = int(number[:i]+number[i+1:])
                res = max(res,tem)
        return str(res)