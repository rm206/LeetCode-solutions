class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, c in enumerate(list(word)):
            if c == ch:
                return word[ : i + 1][::-1] + word[i + 1 : ]
        
        return word