class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        
        n1,n2 = len(nums1), len(nums2)
        i = j = max_res = 0
        
        while i < n1:
            if j < n2 and i <= j and nums1[i] <= nums2[j]: 
                max_res = max(max_res, j-i)
                j += 1
            else: 
                i += 1
                j += 1
                    
        return max_res
    
        """
        n1,n2,res = len(nums1), len(nums2)-1, 0
        
        for j in range(n2,-1,-1):
            tem = 0
            for i in range(0,j+1):
                if i>=n1: break
                if nums1[i]<=nums2[j]:
                    tem = j-i
                    res = max(res,tem)
                    break
                else: 
                    continue
                
        return res
        """