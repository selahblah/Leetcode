class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, tem = [], [] 
        count = {n:0 for n in nums}
        for n in nums:
            count[n] += 1
        
        def dfs():
            if len(tem) == len(nums):
                res.append(tem.copy())
                return
            for n in count:
                if count[n]>0:
                    tem.append(n)
                    count[n] -= 1
                    dfs()
                    count[n] += 1
                    tem.pop()
        dfs()
        return res