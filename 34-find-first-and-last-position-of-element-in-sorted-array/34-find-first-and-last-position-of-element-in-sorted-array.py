class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1,-1]
        
        start = bisect_left(nums,target)
        end = bisect_right(nums,target)
        
        if start == end: return [-1,-1]
        else: return [start,end-1]