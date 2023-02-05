class Solution:
    def trap(self, height: List[int]) -> int:
        height_len = len(height)
        left_max = [0 for _ in range(height_len)]
        right_max = [0 for _ in range(height_len)]
        
        l = height[0]
        for i in range(1, height_len - 1):
            left_max[i] = l
            if height[i] > l:
                l = height[i]
        
        r = height[-1]
        for i in range(height_len - 2, 0, -1):
            right_max[i] = r
            if height[i] > r:
                r = height[i]
        
        res = 0
        for i in range(height_len):
            res += max(min(left_max[i], right_max[i]) - height[i], 0)
        
        return res
        
        


'''
    def trap(self, height: List[int]) -> int:
        heights_len = len(height)
        if heights_len <= 2:
            return 0

        left_maxes = [0 for i in range(heights_len)]
        right_maxes = [0 for i in range(heights_len)]

        left_max = height[0]
        for i in range(1, heights_len-1):
            left_maxes[i] = left_max
            if height[i] > left_max:
                left_max = height[i]

        right_max = height[-1]
        for j in range(heights_len-2, 0, -1):
            right_maxes[j] = right_max
            if height[j] > right_max:
                right_max = height[j]

        sum = 0
        for i in range(1, heights_len-1):
            sum += max(min(left_maxes[i], right_maxes[i])- height[i], 0)

        return sum
'''