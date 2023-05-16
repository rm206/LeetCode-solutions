class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for i, v in enumerate(nums):
            if target - v in numsDict:
                return [numsDict[target - v], i]
            numsDict[v] = i