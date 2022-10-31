class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n in count.keys(): count[n] += 1
            else: count[n] = count.get(n,0) + 1
        count = dict(sorted(count.items(), key = lambda x: x[1], reverse = True))
        print(count)
        return list(count.keys())[:k]