class TrieNode:
    def __init__(self, char):
        self.data = char
        self.children = [None for i in range(26)]
        self.end = False
    
class WordDictionary:

    def __init__(self):
        self.root = TrieNode("")

    def add_util(self, word, root):
        if word == "":
            root.end = True
            return
        
        index = ord(word[0]) - ord('a')
        
        if not root.children[index]:
            child = TrieNode(word[0])
            root.children[index] = child
        else:
            child = root.children[index]
        
        self.add_util(word[1 : ], child)
    
    def addWord(self, word: str) -> None:
        self.add_util(word, self.root)

    def search_util(self, word, root):
        if word == "":
            return root.end
        
        if word[0] == '.':
            for i in range(26):
                if root.children[i] and self.search_util(word[1 : ], root.children[i]):
                    return True
            return False
                    
        else:
            index = ord(word[0]) - ord('a')
            if not root.children[index]:
                return False
            else:
                return self.search_util(word[1 : ], root.children[index])
    
    def search(self, word: str) -> bool:
        return self.search_util(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)