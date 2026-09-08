class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [nums[0]]
        suffix = [nums[-1]]

        for i in range(1, len(nums)):
            prefix.append(nums[i] * prefix[i - 1])
        
        for i in range(len(nums) - 2, -1, -1):
            suffix.append(nums[i] * suffix[-1])
        suffix = suffix[::-1]

        res = []
        for i in range(len(nums)):
            if i - 1 < 0:
                pre = 1
            else:
                pre = prefix[i - 1]
            if i + 1 >= len(nums):
                suf = 1
            else:
                suf = suffix[i + 1]
            res.append(pre*suf)
        return res
