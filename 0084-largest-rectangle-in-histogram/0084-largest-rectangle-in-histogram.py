"""
pse_a = pse()
nse_a = nse()
res = 0
for i, h in enumerate(heights):
    new_height = h * ((nse_a[i]-1) - (pse_a[i]+1) + 1)
    res = max(res, new_height)
return res
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def nse():
            stack = []
            result = [len(heights)] * len(heights)
            for index, val in enumerate(heights):
                while stack and val < stack[-1][1]:
                    p_index, p_val = stack.pop()
                    result[p_index] = index
                
                stack.append([index, val])
            
            return result
        
        def pse():
            stack = []
            result = [-1] * len(heights)
            for index in range(len(heights)-1, -1, -1):
                val = heights[index]
                while stack and val < stack[-1][1]:
                    p_index, p_val = stack.pop()
                    result[p_index] = index
                
                stack.append([index, val])
            
            return result
        
        pse_a = pse()
        nse_a = nse()
        res = 0
        for i, h in enumerate(heights):
            new_height = h * ((nse_a[i]-1) - (pse_a[i]+1) + 1)
            res = max(res, new_height)
        return res