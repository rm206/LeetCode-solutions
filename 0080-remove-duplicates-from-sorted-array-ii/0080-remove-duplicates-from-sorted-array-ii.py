class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_safe = 0
        ptr = 0

        while ptr < len(nums):
            val = nums[ptr]
            nums[last_safe] = val

            last_safe += 1

            if ptr < len(nums) - 1 and nums[ptr+1] == val:
                nums[last_safe] = val
                last_safe += 1

            while ptr < len(nums) and nums[ptr] == val:
                ptr += 1
        
        return last_safe