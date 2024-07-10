class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = [] #will store pairs (index, height)
        maxArea = 0

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                curr_area = height * (i -index)
                maxArea = max(maxArea, curr_area)

                start = index
            stack.append((start, h))
        
        for i, h in stack:
            curr_area = h * (len(heights) - i)
            maxArea = max(maxArea, curr_area)

        return maxArea
    
heights = [2,1,2]
print(Solution().largestRectangleArea(heights))

