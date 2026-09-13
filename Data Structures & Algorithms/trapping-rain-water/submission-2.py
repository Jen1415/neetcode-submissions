class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        water = 0
        left_max = right_max = 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(height[left], left_max)
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(height[right], right_max)
                water += right_max - height[right]
                right -= 1
        return water
        