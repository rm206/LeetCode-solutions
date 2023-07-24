class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        # nums[: n - k] = nums[: n - k].reverse()
        l, r = 0, n - k - 1
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            
        # nums[k + 1 : ] = nums[k + 1 : ].reverse()
        l, r = n - k, n - 1
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        nums.reverse()
        
        
'''        
temp = nums.copy()

for i in range(len(nums)):
    temp[(i + k) % len(nums)] = nums[i]

for i in range(len(temp)):
    nums[i] = temp[i]
'''    