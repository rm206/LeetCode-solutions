class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 2:
            return strs[0]
        
        lens = [len(curr) for curr in strs]
        min_len = min(lens)
        
        i = 0
        broken = False
        res = ""
        while i < min_len and not broken:
            s = [curr[i] for curr in strs]
            if len(set(s)) == 1:
                res += s[0]
            else:
                broken = True
            i += 1
        
        return res
            
        