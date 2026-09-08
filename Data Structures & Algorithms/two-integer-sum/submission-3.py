class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        res = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in res:
                return [res[nums[i]], i]
            res[diff] = i
