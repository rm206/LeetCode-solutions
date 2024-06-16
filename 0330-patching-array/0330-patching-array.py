class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # main point : if some values can sum upto n, adding n + 1 will allow to sum to all vals upto n + (n+1) = 2n + 1

        upto = 0
        i = 0
        patches = 0

        while upto < n:
            if i < len(nums) and nums[i] <= upto + 1:
                upto += nums[i]
                i += 1
            else:
                patches += 1
                upto = upto * 2 + 1

        return patches