class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        comp = {}
        
        for c in s:
            comp[c] = 1 + comp.get(c, 0)
        
        for c in t:
            if c not in comp:
                return False
            
            comp[c] -= 1
            if comp[c] <= 0:
                comp.pop(c)
        
        return comp == {}
        
        

'''
comp  = [0 for i in range(26)]

for c in s:
    comp[ord(c) - ord('a')] += 1

for c in t:
    comp[ord(c) - ord('a')] -= 1

for i in range(26):
    if comp[i] != 0:
        return False

return True
'''