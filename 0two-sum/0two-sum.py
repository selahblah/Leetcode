class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if target-nums[i] in dic: return [dic[target-nums[i]],i]
            else: dic[nums[i]] = i
        
        """
        nums.sort()
        l,r = 0,len(nums)-1
        while l<r:
            if nums[l]+nums[r] > target: r-=1
            elif nums[l]+nums[r] < target: l+=1
            else: return [l,r]
        """