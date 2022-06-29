class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        res = 0
        for i in nums:
            count[i] = count.get(i,0) + 1
        for i in count.values():
            if i>1: res += i*(i-1)//2
        return res
        
        """
        res = 0
        count = Counter(nums)
        for i in count.values():
            if i>1: res += comb(i,2)
        return res
        """
            