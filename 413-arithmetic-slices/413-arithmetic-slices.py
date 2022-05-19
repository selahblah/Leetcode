class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        if len(nums)<3: return 0
        
        diff = []
        count, res= 1, 0
        for i in range(1,len(nums)):
            diff.append(nums[i]-nums[i-1])
        for j in range(len(diff)-1):
            if diff[j] == diff[j+1]: 
                res += count
                count += 1
            else: 
                count = 1
            
        return res
        
        