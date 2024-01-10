class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        def conc(n1, n2):
            return int(str(n1)+str(n2))
        
        res = 0
        l, r = 0, len(nums) - 1
        
        while l <= r:
            if l != r:
                res += conc(nums[l], nums[r])
                l += 1
                r -= 1
            else:
                res += nums[l]
                break
        
        return res