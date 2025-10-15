class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def check(index):
            curr = -math.inf
            for j in range(index, index+k):
                if nums[j] <= curr:
                    return False
                curr = nums[j]
            return True

        if len(nums) < 2 * k:
            return False
        
        for i in range(len(nums) - 2*k + 1):
            if check(i) and check(i+k):
                return True
        
        return False