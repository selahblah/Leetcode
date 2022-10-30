class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic.keys(): return [dic[target - nums[i]],i]
            else: dic[nums[i]] = i
        """
        for i in range(len(nums)-1):
            if target - nums[i] in nums[i+1:]: return [i, nums.index(target - nums[i])]
        """