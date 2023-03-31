class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        c = 1
        for i in range(1, len(nums)):
            if nums[i] == candidate:
                c += 1
            elif nums[i] != candidate:
                c -= 1
            
            if c == 0:
                candidate = nums[i]
                c = 1
        
        return candidate