class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        l, r = 0, 0
        run_sum = 0
        res = 0

        for r in range(len(nums)):
            run_sum += nums[r]

            # shrink the window to make this possible
            while nums[r]*(r-l+1) - run_sum > k:
                run_sum -= nums[l]
                l += 1

            res = max(res, r-l+1)
        
        return res