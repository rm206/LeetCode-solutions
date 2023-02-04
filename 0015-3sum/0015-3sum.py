import collections

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        len_nums = len(nums)
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i + 1, len_nums-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                
                if threeSum > 0:
                    r -= 1
                    
                elif threeSum < 0:
                    l += 1
                
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        return res



'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set({})
        len_nums = len(nums)
        num_map = collections.defaultdict(set)
        for i, v in enumerate(nums):
            num_map[v].add(i)

        for i in range(0, len_nums):
            for j in range(i+1, len_nums):
                to_find = (-1)*(nums[i]+nums[j])
                if to_find in num_map and ((i not in num_map[to_find] and j not in num_map[to_find]) or len(num_map[to_find])>2):
                    res.add(tuple(sorted([nums[i], nums[j], to_find])))

        new_res = [list(curr) for curr in res]
        return new_res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        len_nums = len(nums)
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i + 1, len_nums-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                
                if threeSum > 0:
                    r -= 1
                    
                elif threeSum < 0:
                    l += 1
                
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        return res
'''