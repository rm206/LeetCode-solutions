class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        h = len(height)
        
        maxes = [0 for i in range(h)]
        l = height[0]
        for i in range(1, h-1):
            maxes[i] = l
            l = max(l, height[i])
        
        r = height[-1]
        for i in range(h - 2, 0, -1):
            maxes[i] = min(r, maxes[i])
            r = max(r, height[i])
            
        res = 0
        for i in range(1, h-1):
            res += max(maxes[i] - height[i], 0)
        
        return res