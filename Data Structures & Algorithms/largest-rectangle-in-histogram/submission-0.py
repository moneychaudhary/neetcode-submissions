class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        total_bars = len(heights)
        right_smallest = [total_bars] * total_bars
        left_smallest = [-1] * total_bars

        stack = []
        for i in range(total_bars - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                right_smallest[i] = stack[-1]
            stack.append(i)

        while stack:
            stack.pop()

        for i in range(total_bars):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                left_smallest[i] = stack[-1]
            stack.append(i)
        
        print(left_smallest)
        print(right_smallest)
        max_area = 0
        for i in range(total_bars):
            width = right_smallest[i] - left_smallest[i] - 1
            max_area = max(max_area, width * heights[i])

        return max_area

