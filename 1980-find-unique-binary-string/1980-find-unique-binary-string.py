class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        def builder(n, s):
            if len(s) == n:
                res.append(s)
                return
            
            s += '0'
            builder(n, s)
            s = s[:-1]
            s += '1'
            builder(n, s)
        
        res = []
        builder(len(nums[0]), "")
        
        return list(set(res) - set(nums))[0]