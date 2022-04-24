class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        del nums1[m:]
        nums1 += nums2[:n]
        
        nums1.sort()
        
        """
        for i in range(n):
            nums1=nums1[:m+i]
            nums1.append(nums2[i])
        
        nums1.sort()
        """
        return nums1