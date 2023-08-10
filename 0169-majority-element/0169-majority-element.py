class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = nums[0]
        c = 1
        
        for i in range(1, len(nums)):
            if nums[i] == cand:
                c += 1
            else:
                c -= 1
            
            if c == 0:
                cand = nums[i]
                c = 1
        
        return cand

'''
l= len(nums)
c = {}

for n in nums:
    c[n] = 1 + c.get(n, 0)
    if c[n] > (l// 2):
        return n
'''
            