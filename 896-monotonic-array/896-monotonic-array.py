class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        dec = inc = True
        pre = nums[0]
        for n in nums[1:]:
            if pre > n: dec = False
            elif pre < n: inc = False
            pre = n 
            if dec == False and inc == False: return False
        return True