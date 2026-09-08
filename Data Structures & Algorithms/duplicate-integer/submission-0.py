class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        num_qty = {}
        for num in nums:
            if num in num_qty:
                num_qty[num] = 1
            else:
                num_qty[num] = 0

        return any(num_qty.values())