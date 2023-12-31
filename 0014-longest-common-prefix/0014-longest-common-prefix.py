class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        l = min([len(s) for s in strs])
        
        res = ""
        for i in range(l):
            char = strs[0][i]
            
            for s in strs[1:]:
                if s[i] != char:
                    return res
            
            res = res + char
        
        return res