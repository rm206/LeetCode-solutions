class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l= len(nums)
        c = {}
        
        for n in nums:
            c[n] = 1 + c.get(n, 0)
            if c[n] > (l// 2):
                return n
            