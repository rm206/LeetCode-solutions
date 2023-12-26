class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        real_sum = sum(nums)
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2
        
        return expected_sum - real_sum