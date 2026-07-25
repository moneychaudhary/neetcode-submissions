class Solution:
    def maxArea(self, heights: List[int]) -> int:
        total_heights = len(heights)
        start = 0
        end = total_heights - 1
        max_area = 0

        while start < end:
            width = end - start
            height = min(heights[start], heights[end])
            total_area = width * height
            max_area = max(max_area, total_area)
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        return max_area
        