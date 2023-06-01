class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def calc_prev_smaller_elt(arr, n):
            nonlocal heights
            stack = []
            stack.append(-1)
            for i in range(0, n):
                while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                arr[i] = stack[-1]
                stack.append(i)
                
        def calc_next_smaller_elt(arr, n):
            nonlocal heights
            stack = []
            stack.append(-1)
            for i in range(n-1, -1, -1):
                while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                arr[i] = stack[-1]
                stack.append(i)
            
        
        res = -1
        prev_smaller_elt = [-1 for i in range(len(heights))]
        next_smaller_elt = [-1 for i in range(len(heights))]
        calc_prev_smaller_elt(prev_smaller_elt, len(heights))
        calc_next_smaller_elt(next_smaller_elt, len(heights))
        
        for i in range(len(heights)):
            if next_smaller_elt[i] == -1:
                next_smaller_elt[i] = len(heights)
            curr_area = heights[i] * (next_smaller_elt[i] - prev_smaller_elt[i] - 1)
            res = max(res, curr_area)
        
        return res