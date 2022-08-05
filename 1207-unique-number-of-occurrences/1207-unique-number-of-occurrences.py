class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        key, value = list(c.keys()), list(c.values())
        return len(key) == len(set(value))