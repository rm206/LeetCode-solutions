class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, index = 0, len(nums) - 1
        while i <= index:
            if nums[i] == val:
                nums[i], nums[index] = nums[index], nums[i]
                index -= 1
            else:
                i += 1
        
        return i

'''
i, index = 0, len(nums) - 1
while i < index:
    if nums[i] == val:
        nums[i], nums[index] = nums[index], nums[i]
        index -= 1
        while nums[i] == val:
            nums[i], nums[index] = nums[index], nums[i]
            index -= 1
    i += 1

return i + 1

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
'''