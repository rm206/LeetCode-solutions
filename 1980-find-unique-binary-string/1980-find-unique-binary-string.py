class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = ""

        for i, n in enumerate(nums):
            res += str(1 - int(n[i]))
        
        return res