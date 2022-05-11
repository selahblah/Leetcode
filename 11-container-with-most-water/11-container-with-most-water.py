class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_s = 0
        left, right = 0, len(height)-1
        
        while left < right:
            max_s = max(max_s, (right-left)*(min(height[right],height[left])))
            
            if height[right] < height[left]:
                right -=1
            else:
                left += 1
        
        return max_s
        
        """
        max_s = 0
        for i in range(len(height)-1):
            right = len(height)-1
            while i < right:
                max_s = max(max_s, (right-i)*min(height[i],height[right]))
                right -= 1
        return max_s
        """     
        