class Solution:
    def trap(self, height: list[int]) -> int:
        water = 0
        stack = []
        
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                top = stack.pop()
                if not stack:
                    break
                floor = height[top]
                right_wall = height[i]
                left_wall = height[stack[-1]]   
                water += (min(left_wall, right_wall) - floor) * (i - stack[-1] - 1)    
            stack.append(i)
        return water
        