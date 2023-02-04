import collections

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