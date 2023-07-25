from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        
        if l1 > l2:
            return False
        
        l, r = 0, l1 - 1
        d1 = Counter(s1)
        
        while r < l2:
            if Counter(s2[l : r + 1]) == d1:
                return True
            l += 1
            r += 1
        
        return False
#         l1, l2 = len(s1), len(s2)
        
#         if l1 > l2:
#             return False
        
#         l, r = 0, 0
#         d1, d2 = {}, {}
        
#         for c in s1:
#             d1[c] = 1 + d1.get(c, 0)
        
#         while r < l2:
#             # fix window and dictionary it is longer than s1
#             if r - l + 1 > l1:
#                 if d2[s2[l]] > 1:
#                     d2[s2[l]] -= 1
#                 else:
#                     d2.pop(s2[l])
#                 l += 1
            
#             d2[s2[r]] = 1 + d2.get(s2[r], 0)
            
#             # compare dicts with the current corrected window
#             if d1 == d2:
#                 return True
            
#             r += 1
        
#         return False