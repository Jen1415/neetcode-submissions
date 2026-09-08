class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            middle = low + (high - low) // 2
            if nums[middle] < target:
                low = middle + 1
            elif nums[middle] > target:
                high = middle - 1
            else:
                return middle
        return -1
