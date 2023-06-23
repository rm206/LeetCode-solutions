class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        forward_mapping = {}
        backward_mapping = {}
        for i in range(len(s)):
            if s[i] not in forward_mapping:
                if t[i] not in backward_mapping:
                    forward_mapping[s[i]] = t[i]
                    backward_mapping[t[i]] = s[i]
                else:
                    return False
            else:
                if t[i] != forward_mapping[s[i]]:
                    return False
        
        return True