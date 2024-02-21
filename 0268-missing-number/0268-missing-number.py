class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_sum = 0
        n = len(nums)
        for i in range(n):
            xor_sum ^= i ^ nums[i]
        return xor_sum ^ n