class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        total = 0
        sub = 0
        left = 0
        cur_product = 1
    
        for i in range(len(nums)):
            cur_product *= nums[i]
            sub += 1
            
            while cur_product >= k and left < i:
                cur_product /= nums[left]
                left += 1
                sub -= 1
            
            if cur_product < k:
                total += sub
        
        return total
        
                
                
            
        
        
        
        
        
        
        for i in range(len(nums)):         
            tem = []
            j=0
            while i+j < len(nums):
                tem.append(nums[i+j])
                if numpy.prod(tem) >= k: 
                    tem=[]
                    continue
                elif i+j == len(nums)-1: 
                    count += 1
                    tem.append(nums[i+j])
                    j += 1
                else: 
                    count += 1
                    j += 1
                    
            return count