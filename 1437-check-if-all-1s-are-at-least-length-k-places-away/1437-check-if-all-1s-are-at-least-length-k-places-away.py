class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        i = 0
        while i < len(nums) and nums[i] != 1:
            i += 1
        
        prev = i
        curr = prev + 1

        while curr < len(nums):
            if nums[curr] == 1:
                if curr-prev-1 < k:
                    return False
                prev = curr
            
            curr += 1
        
        return True