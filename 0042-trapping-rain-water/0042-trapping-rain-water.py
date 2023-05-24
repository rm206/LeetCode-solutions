class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        left = [0 for i in range(len(height))]
        right = [0 for i in range(len(height))]
        left_max = height[0]
        right_max = height[len(height) - 1]
        
        for i in range(1, len(height)):
            left[i] = left_max
            left_max = max(left_max, height[i])
        
        for i in range(len(height) - 2, -1, -1):
            right[i] = right_max
            right_max = max(right_max, height[i])
        
        mixed = [0 for i in range(len(height))]
        for i in range(len(height)):
            mixed[i] = max(0, min(left[i], right[i]) - height[i])
        
        res = 0
        for i in range(1, len(height) - 1):
            res += mixed[i]
        
        return res