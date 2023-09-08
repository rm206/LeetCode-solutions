class TextEditor:

    def __init__(self):
        self.left = []
        self.right = []

    def addText(self, text: str) -> None:
        for c in text:
            self.left.append(c)

    def deleteText(self, k: int) -> int:
        count = 0
        while self.left and k:
            self.left.pop()
            k -= 1
            count += 1
        
        return count
    
    def left_chars(self):
        res = ""
        
        l = min(10, len(self.left))
        
        return "".join(self.left[- l : ])
    
    def cursorLeft(self, k: int) -> str:
        while self.left and k:
            c = self.left.pop()
            self.right.append(c)
            k -= 1
        
        return self.left_chars()

    def cursorRight(self, k: int) -> str:
        while self.right and k:
            c = self.right.pop()
            self.left.append(c)
            k -= 1
        
        return self.left_chars()


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)