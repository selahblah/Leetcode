class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums is None or nums==[0]: return []
        
        nums.sort()
        res=[]
        
        for i, a in enumerate(nums):
            
            if i > 0 and a == nums[i-1]:
                continue
            
            left = i+1
            right = len(nums)-1
        
            while left < right:
                tem = a + nums[left] + nums[right]
                if tem < 0:
                    left += 1
                elif tem > 0:
                    right -= 1
                else:
                    res.append([a,nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left +=1
                    
        return res
                