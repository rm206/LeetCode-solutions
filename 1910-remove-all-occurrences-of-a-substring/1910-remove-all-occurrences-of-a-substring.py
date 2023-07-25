class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        part_len = len(part)
        n = len(s)
        i = 0
        
        while i < n:
            if i + part_len - 1 < n and s[i : i + part_len] == part:
                temp = s[ : i] + s[i + part_len : ]
                s = temp
                n -= part_len
                i = 0
            else:
                i += 1
        
        return s