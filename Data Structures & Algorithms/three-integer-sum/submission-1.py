
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            target = -1 * nums[i]
            while l < r:             
                if (nums[l] + nums[r] == target):
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[r] + nums[l] > target:
                    r -= 1
                else:
                    l += 1
        return res
