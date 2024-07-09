class Solution:
    def compress(self, chars: List[str]) -> int:
        res = ""
        res_len = 0
        ctr = 0
        curr = chars[0]

        for c in chars:
            if c == curr:
                ctr += 1
            else:
                if ctr == 1:
                    res = res + curr
                    res_len += 1
                else:
                    res = res + curr + str(ctr)
                    res_len += 1 + len(str(ctr))
                curr = c
                ctr = 1
        if ctr == 1:
            res = res + curr
            res_len += 1
        else:
            res = res + curr + str(ctr)
            res_len += 1 + len(str(ctr))
        
        i = 0
        for c in res:
            chars[i] = c
            i += 1
        
        return res_len