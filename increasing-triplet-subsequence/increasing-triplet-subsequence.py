class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        if len(nums)<3: return False
        smallest = mid = float("inf")
        for n in nums:
            if n <= smallest: smallest = n
            elif n <= mid: mid = n
            else: return True
        return False
        
        """
        tem = [nums[0]]
        for n in nums[1:]:
            x = bisect_left(tem,n)
            if x == len(tem): tem.append(n)
            elif x < len(tem): tem[x] = n
            if len(tem) == 3: return True 
        return False
        """