class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        s = {}
        
        for i in range(len(nums)):
            s[nums[i]] = 1 + s.get(nums[i], 0)

        res = 0
        for k, v in s.items():
            n = v - 1
            res += (n * (n + 1)) // 2
        
        return res