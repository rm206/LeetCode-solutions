class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = []
        curr = 1
        
        for n in nums:
            curr *= n
            prefix.append(curr)
            if curr == 0:
                curr = 1
        
        suffix = [None for i in range(len(nums))]
        
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            prod *= nums[i]
            suffix[i] = prod
            if prod == 0:
                prod = 1
        
        return max(max(prefix), max(suffix))