class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # first
        # set = {}
        # for index, val in enumerate(nums):
        #     if target-val in set:
        #         return [index, set[target-val]]
        #     set[val] = index
        
        #23 nov 2022
        # s = {}
        # for i,v in enumerate(nums):
        #     if target-v in s:
        #         return [i, s[target-v]]
        #     s[v] = i
        # Jan 9
        s = {}
        for i, v in enumerate(nums):
            if target - v in s:
                return [i, s[target - v]]
            s[v] = i