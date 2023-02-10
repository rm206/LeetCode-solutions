class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        len_nums = len(nums)
        if len_nums == 0:
            return 0
        
        start, end = 0, len_nums - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
            else:
                start += 1
        
        return start
        