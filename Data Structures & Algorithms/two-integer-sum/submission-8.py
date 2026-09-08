class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        diff = {}
        for num in range(len(nums)):
            if nums[num] in diff:
                return[diff[nums[num]], num]
            diff[target - nums[num]] = num


