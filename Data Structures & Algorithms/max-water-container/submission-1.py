class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l, r = 0, len(heights) - 1
        max_unit = 0
        while l < r:
            max_unit = max((r - l) * (min(heights[l], heights[r])), max_unit)
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return max_unit
                