class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3: return False
        smallest = mid = float("inf")
        for n in nums:
            if n <= smallest: smallest = n
            elif n <= mid: mid = n
            else: return True
        return False