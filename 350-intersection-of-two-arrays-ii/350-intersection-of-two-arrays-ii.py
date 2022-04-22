class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        return list((Counter(nums1) & Counter(nums2)).elements())
        
        """
        if not nums1 or not nums2:
            return []
        
        
        res = []
        
        x = collections.Counter(nums1)
        y = collections.Counter(nums2)
        
        for key,value in x.items():
            if key in y:
                n = min(value,y[key])
                for i in range(n):
                    res.append(key)
        return res
        """
        
        
        """
        result = []
        for i in nums1:
            if i in nums2:
                result.append(i)
                nums2.remove(i)
                    
        return result
        """
            
        