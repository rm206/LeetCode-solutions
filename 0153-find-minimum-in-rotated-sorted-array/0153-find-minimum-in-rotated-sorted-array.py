class Solution:
    def findMin(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
        
#         l, r = 0, len(nums) - 1
#         while l < r:
#             mid = (l+r) // 2
#             if nums[mid] < nums[mid - 1]:
#                 return nums[mid]
#             elif nums[mid] > nums[r]:
#                 l = mid + 1
#             else:
#                 r = mid - 1
        return min(nums)
#         l, r = 0, len(nums) - 1
#         res = nums[0]
        
#         while l <= r:
#             if nums[l] < nums[r]:
#                 res = min(res, nums[l])
#                 return res
            
#             mid = (l + r) // 2
#             res = min(res, nums[mid])
#             if nums[mid] >= nums[l]:
#                 l = mid + 1
#             else:
#                 r = mid - 1
        
#         return res
        