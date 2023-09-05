class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        h = len(height)
        
        left_max = [0 for i in range(h)]
        l = height[0]
        for i in range(1, h):
            left_max[i] = l
            l = max(l, height[i])
        
        right_max = [0 for i in range(h)]
        r = height[-1]
        for i in range(h - 2, -1, -1):
            right_max[i] = r
            r = max(r, height[i])
        
        res = 0
        for i in range(h):
            res += max(min(left_max[i], right_max[i]) - height[i], 0)
        
        return res