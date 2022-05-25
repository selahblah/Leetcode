class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        
        for n in range(nums[-1],-1,-1):
            x = bisect_left(nums,n)
            if n == l-x: return n 
        
        return -1
        
        