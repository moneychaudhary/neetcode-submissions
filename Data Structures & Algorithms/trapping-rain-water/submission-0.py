class Solution:
    def trap(self, height: List[int]) -> int:
        total_bars = len(height)
        left_max = [0] * total_bars
        right_max = [0] * total_bars
        left_max[0] = height[0]
        right_max[total_bars - 1] = height[total_bars - 1 ]

        for i in range(1, total_bars):
            left_max[i] = max(left_max[i - 1], height[i])
        
        for i in range(total_bars-2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
        total_water = 0
        for i in range(total_bars):
            total_water += min(left_max[i], right_max[i]) - height[i]
        
        return total_water


            
        