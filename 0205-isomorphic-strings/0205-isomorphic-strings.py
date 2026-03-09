class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st = {}
        ts = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            if char_s in st and st[char_s] != char_t:
                return False
            
            if char_t in ts and ts[char_t] != char_s:
                return False
            
            st[char_s] = char_t
            ts[char_t] = char_s
        
        return True

        # e g g
        # a d b
        """
        e a | a e
        g d | d g
            | b g
        """