class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        forward_mapping = {}
        backward_mapping = {}
        for i in range(len(s)):
            cs, ct = s[i], t[i]

            if (cs in forward_mapping and forward_mapping[cs] != ct) or (ct in backward_mapping and backward_mapping[ct] != cs):
                return False

            forward_mapping[cs] = ct
            backward_mapping[ct] = cs
        
        return True


'''
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
'''