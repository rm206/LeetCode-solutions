class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxw = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            maxw = max(maxw, min(height[l], height[r]) * (r - l))
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxw


'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxw = 0
        for i in range(0, len(height)):
            for j in range(i+1, len(height)):
                maxw = max(maxw, min(height[i], height[j])*(j-i))
        
        return maxw
'''