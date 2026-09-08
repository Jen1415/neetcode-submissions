class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        bucket = {} # freq -> [nums]
        for num in nums:
            if num not in bucket:
                bucket[num] = 1
            else:
                bucket[num] += 1

        bucket = dict(sorted(bucket.items(), key=lambda x: x[1], reverse=True))
        ans = list(bucket.keys())[0: k]
        return ans
