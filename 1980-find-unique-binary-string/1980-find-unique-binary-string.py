class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        def builder(n, s):
            if len(s) == n:
                if s not in set_nums:
                    res.append(s)
                return
            
            s += '0'
            builder(n, s)
            s = s[:-1]
            s += '1'
            builder(n, s)
            s = s[:-1]
        
        res = []
        set_nums = set(nums)
        builder(len(nums[0]), "")
        
        return res[0]