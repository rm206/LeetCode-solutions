class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            parent = strs[0][i]
            
            for s in range(1, len(strs)):
                if i == len(strs[s]) or strs[s][i] != parent:
                    return res
            
            res += parent
        
        return res