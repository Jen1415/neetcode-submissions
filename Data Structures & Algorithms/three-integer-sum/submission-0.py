
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            l, r = 0, len(nums) - 1
            target = -1 * nums[i]
            while l < r:
                if l == i:
                    l += 1
                    continue
                if r == i:
                    r -= 1
                    continue                
                if (nums[l] + nums[r] == target) and (sorted([nums[l], nums[r], nums[i]]) not in res):
                    res.append(sorted([nums[l], nums[r], nums[i]]))
                elif nums[r] + nums[l] > target:
                    r -= 1
                else:
                    l += 1
        return res
