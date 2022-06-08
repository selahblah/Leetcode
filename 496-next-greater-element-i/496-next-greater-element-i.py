class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        stack = [nums2[0]]
        for i in range(1,len(nums2)):
            while stack and stack[-1]<nums2[i]:
                dic[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        for j in stack:
            dic[j] = -1
            
        return [dic[key] for key in nums1]