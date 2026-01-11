class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        # 각 열의 연속된 1의 높이
        heights = [0] * cols
        max_area = 0

        for r in range(rows):
            # 히스토그램 만들기
            for c in range(cols):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0

            # 현재 히스토그램에서 최대 직사각형
            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0

        for i in range(len(heights) + 1):
            h = 0 if i == len(heights) else heights[i]

            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area
