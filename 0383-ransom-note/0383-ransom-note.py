class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        comp = [0 for i in range(26)]
        
        for c in magazine:
            comp[ord(c) - ord('a')] += 1
        
        for c in ransomNote:
            if comp[ord(c) - ord('a')] <= 0:
                return False
            comp[ord(c) - ord('a')] -= 1
        
        return True