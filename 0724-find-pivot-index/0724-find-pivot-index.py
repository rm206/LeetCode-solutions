class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum, rsum = 0, sum(nums)

        for i in range(len(nums)):
            rsum -= nums[i]

            if lsum == rsum:
                return i
            
            lsum += nums[i]

        return -1