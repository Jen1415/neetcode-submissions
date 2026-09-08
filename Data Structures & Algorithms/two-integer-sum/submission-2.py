class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        tracker = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp not in tracker:
                tracker[nums[i]] = i
            else:
                return [tracker[comp], i]
