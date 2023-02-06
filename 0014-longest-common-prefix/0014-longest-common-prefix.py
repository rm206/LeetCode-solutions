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
            # s = [curr[i] for curr in strs]
            s = set({})
            for curr in strs:
                s.add(curr[i])
            if len(s) == 1:
                # res += s[0]
                res += strs[0][i]
            else:
                broken = True
            i += 1
        
        return res
            
        