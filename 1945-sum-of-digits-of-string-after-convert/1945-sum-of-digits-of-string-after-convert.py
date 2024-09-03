class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def convert_str(string):
            res = ""
            for c in string:
                res = res + str(ord(c) - ord('a') + 1)
            return res
        
        def transform(string):
            res = 0

            for c in string:
                res += int(c)
            
            return str(res)

        s = convert_str(s)

        for _ in range(k):
            s = transform(s)
        
        return int(s)