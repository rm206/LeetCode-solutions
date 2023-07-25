class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 0 
        s = []
        
        while i < n:
            c = chars[i]
            counter = 0
            
            while i < n and chars[i] == c:
                counter += 1
                i += 1
            
            s.append(c)
            if counter > 1:
                s.extend(list(str(counter)))
        
        for i in range(len(s)):
            chars[i] = s[i]
        return len(s)