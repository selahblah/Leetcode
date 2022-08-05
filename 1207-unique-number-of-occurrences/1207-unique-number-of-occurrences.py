class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        key, value = list(c.keys()), list(c.values())
        return len(set(key)) == len(set(value))