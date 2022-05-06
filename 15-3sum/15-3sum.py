class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            left, right = i+1, len(nums)-1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([a,nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return res
        
        """
        for i in nums:
            nums.remove(i)
            print(nums)
            while left < right:
                if nums[left] + nums[right] == -i:
                    tem.extend([nums[left], nums[right], i])
                    res.append(tem)
                elif nums[left] + nums[right] > -i:
                    right -= 1
                else:
                    left += 1
                    
        return res
        """