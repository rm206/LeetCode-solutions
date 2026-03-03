class Node:
    def __init__(self):
        self.arr = [None] *26
        self.flag = False
    
    def has_key(self, char):
        return self.arr[ord(char) - ord('a')] is not None
    
    def set_char(self, char, newnode):
        self.arr[ord(char) - ord('a')] = newnode
    
    def get_char(self, char):
        return self.arr[ord(char) - ord('a')]
    
    def end_word(self):
        self.flag = True
    
    def is_end_of_word(self):
        return self.flag

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if not node.has_key(c):
                newnode = Node()
                node.set_char(c, newnode)
                node = newnode
            else:
                node = node.get_char(c)
        
        node.end_word()

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if not node.has_key(c):
                return False
            else:
                node = node.get_char(c)
        
        return node.is_end_of_word()

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if not node.has_key(c):
                return False
            else:
                node = node.get_char(c)
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)