class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <3 or nums == [0]: return []
        
        nums = sorted(nums)
        res = []
        i=0
        
        while i < len(nums)-2:
            if i>0 and nums[i] == nums[i-1]: 
                i += 1
                continue
                
            left = i + 1
            right = len(nums)-1
            while left < right:
                summ = nums[left] + nums[right] + nums[i]
                if summ == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif summ < 0:
                    left += 1
                else: right -= 1  
            i += 1
                
        return res