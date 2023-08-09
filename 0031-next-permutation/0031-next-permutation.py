class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        break_point = -1
        n = len(nums)
        
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break_point = i
                break

        if break_point == -1:
            nums.reverse()
            return nums
        
        for i in range(n - 1, break_point, -1):
            if nums[i] > nums[break_point]:
                nums[i], nums[break_point] = nums[break_point], nums[i]
                break
        
        temp1 = nums[ : break_point + 1]
        temp2 = nums[break_point + 1 : ]
        temp2.reverse()
        temp = temp1 + temp2
        
        for i in range(n):
            nums[i] = temp[i]