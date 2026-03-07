class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atmost(target):
            if target < 0:
                return 0
            l, r = 0, 0
            run_sum = 0
            cnt = 0
            for r in range(len(nums)):
                run_sum += nums[r]
                while run_sum > target:
                    run_sum -= nums[l]
                    l += 1
                if run_sum <= goal:
                    cnt += (r - l + 1)
            return cnt
        
        return atmost(goal) - atmost(goal - 1)