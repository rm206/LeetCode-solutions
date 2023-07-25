class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        arr.reverse()
        res = " ".join(arr)
        
        return res
                    