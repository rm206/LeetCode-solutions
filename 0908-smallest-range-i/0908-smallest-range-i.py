class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        mini = min(nums) + k
        maxi = max(nums) - k
        
        return max(0, maxi-mini)