class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        has = []
        
        for i in nums:
            if not i in has:
                has.append(i)
            else:
                has.remove(i)
        return has[0]