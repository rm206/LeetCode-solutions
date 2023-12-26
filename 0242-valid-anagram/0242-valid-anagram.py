class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        al_s = [0 for i in range(26)]
        al_t = [0 for i in range(26)]
        
        for c in s:
            al_s[ord(c) - ord('a')] += 1
        for c in t:
            al_t[ord(c) - ord('a')] += 1
        
        return al_s == al_t