class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        n = len(s) - 1
        builder = []
        
        while i <= n:
            while i <= n and s[i] == ' ':
                i += 1
            
            if i <= n:
                word = ""

                while i <=n and s[i] != ' ':
                    word += s[i]
                    i += 1

                builder.append(word)
        
        res = ""
        for i in range(len(builder) - 1, -1, -1):
            res += builder[i]
            if n > 1 and i != 0:
                res += " "
        
        
        return res
        

'''
arr = s.split()
arr.reverse()
res = " ".join(arr)

return res
'''
                    