import copy
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        
        if l == 1:
            return False
        
        
        build = []
        for i in range(l - 1):
            build.append([s[ : i + 1], l // (i + 1)])
        
        for string, length in build:
            if string * length == s:
                print("True on string : ", string)
                return True
        return False