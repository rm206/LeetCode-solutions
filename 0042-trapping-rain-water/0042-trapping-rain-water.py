class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        if n < 3:
            return 0
            
        lefts = [0 for i in range(n)]
        rights = [0 for i in range(n)]
        max_l = height[0]
        max_r = height[n - 1]
        
        
        for l in range(1, n - 1):
            lefts[l] = max_l
            max_l = max(max_l, height[l])
        
        for r in range(n-2, 0, -1):
            rights[r] = max_r
            max_r = max(max_r, height[r])
        
        res = 0 
        for i in range(1, n - 1):
            res += max(min(lefts[i], rights[i]) - height[i], 0)
        
        return res