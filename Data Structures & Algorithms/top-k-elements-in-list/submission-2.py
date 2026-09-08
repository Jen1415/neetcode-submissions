class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # nums = [1,2,2,3,3,3], k = 2
        from collections import Counter
        counts = dict(Counter(nums))
        sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
        res = list(sorted_counts.keys())
        return res[0: k]