class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_map = Counter(arr)
        return len(set(freq_map.values())) == len(freq_map)