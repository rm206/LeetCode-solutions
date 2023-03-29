class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums+nums
#         ans = []
#         n = len(nums)
#         for i in range(0, n):
#             ans.append(nums[i])
#         for i in range(n, 2*n):
#             ans.append(nums[i-n])
        
#         return ans