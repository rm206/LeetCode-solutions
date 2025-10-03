class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        max_possible = min([len(s) for s in strs])

        if max_possible == 0:
            return ""
        
        res = ""

        for i in range(max_possible):
            char = strs[0][i]

            for s in strs[1:]:
                if char != s[i]:
                    return res
            
            res += char
        
        return res
