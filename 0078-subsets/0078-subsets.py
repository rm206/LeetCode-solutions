import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def solver(arr, incoming):
            nonlocal res

            templist = copy.copy(incoming)
            res.append(templist)
            for i in range(len(arr)):
                incoming.append(arr[i])
                solver(arr[i+1:], incoming)
                incoming.pop()
        
#         def solver(i):
#             nonlocal nums, subset, res

#             if i >= len(nums):
#                 res.append(subset.copy())
#                 return
            
#             subset.append(nums[i])
#             solver(i + 1)

#             subset.pop()
#             solver(i + 1)
            

        # subset = []
        res = []
        solver(nums, [])
        # solver(0)
        return res