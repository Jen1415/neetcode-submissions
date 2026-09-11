class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l, r = 0, len(heights) - 1
        max_unit = (r - l) * (min(heights[l], heights[r]))
        while l < r:
            if heights[r] > heights[l]:
                l += 1
                max_unit = max((r - l) * (min(heights[l], heights[r])), max_unit)
            else:
                r -= 1
                max_unit = max((r - l) * (min(heights[l], heights[r])), max_unit)
        return max_unit
                