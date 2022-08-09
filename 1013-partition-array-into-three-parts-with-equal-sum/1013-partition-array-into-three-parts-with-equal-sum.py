class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr)%3: return False
        target = sum(arr)//3
        cur = res = 0
        for n in arr:
            cur += n
            if cur == target:
                res += 1
                cur = 0
            print(res)
        return True if res >= 3 else False