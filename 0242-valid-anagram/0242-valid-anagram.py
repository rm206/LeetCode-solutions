class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Nov 27, 2022
        # map1 = {}
        # for i in s:
        #     if i not in map1:
        #         map1[i] = 1
        #     else:
        #         map1[i] += 1
        
        # map2 = {}
        # for i in t:
        #     if i not in map2:
        #         map2[i] = 1
        #     else:
        #         map2[i] += 1
        
        # if(len(map1) != len(map2)):
        #     return False
        # if(map1.keys() != map2.keys()):
        #     return False
        
        # for i in map1:
        #     if map1[i] != map2[i]:
        #         return False
        
        # return True
    
#             if len(s) != len(t):
#             return False

#         countS, countT = {}, {}

#         for i in range(len(s)):
#             countS[s[i]] = 1 + countS.get(s[i], 0)
#             countT[t[i]] = 1 + countT.get(t[i], 0)
#         return countS == countT

        # Jan 14
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT