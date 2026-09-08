class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap = {}
        for index, value in enumerate(nums):
            hashMap[value] = index
        for index, value in enumerate(nums):
            diff = target - value
            if diff in hashMap and hashMap[diff] != index:
                return [index, hashMap[diff]]

        return []   


        