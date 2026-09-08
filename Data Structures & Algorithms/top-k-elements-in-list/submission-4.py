class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from collections import Counter
        counts = dict(Counter(nums))
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, value in counts.items():
            buckets[value].append(key)
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i]:
                for bucket in buckets[i]:
                    res.append(bucket)
                    if len(res) == k:
                        return res