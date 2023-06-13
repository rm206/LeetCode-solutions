class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        min_len = len(strs[0])
        for s in strs:
            min_len = min(len(s), min_len)
        
        for i in range(min_len):
            for s in strs:
                if s[i] != strs[0][i]:
                    return res
            res += s[i]
        
        return res