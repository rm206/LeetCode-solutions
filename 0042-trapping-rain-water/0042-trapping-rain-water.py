class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        lmax, rmax = height[l], height[r]
        res = 0

        while l < r:
            if lmax <= rmax:
                l += 1
                res += max(min(lmax, rmax)-height[l], 0)
                lmax = max(lmax, height[l])
            else:
                r -= 1
                res += max(min(lmax, rmax)-height[r], 0)
                rmax = max(rmax, height[r])
        
        return res