class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0

        res = 0
        nums.sort()
        k = abs(k)
        l, r = 0, 1

        while l < len(nums) and r < len(nums):
            diff = abs(nums[l] - nums[r])

            if diff == k:
                res += 1
                val = nums[l]
                l += 1
                while l < len(nums) and nums[l] == val:
                    l += 1            
            elif diff < k:
                r += 1
            else:
                l += 1

            if l >= r:
                r = l + 1
        
        return res