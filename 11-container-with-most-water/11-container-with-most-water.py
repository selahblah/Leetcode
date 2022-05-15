class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        max_s = 0
        left, right = 0, len(height)-1
        
        while left < right:
            max_s = max(max_s, (right-left)*min(height[left],height[right]))
            if height[left] < height[right]:
                left += 1
            else: right -= 1
            
        return max_s
            