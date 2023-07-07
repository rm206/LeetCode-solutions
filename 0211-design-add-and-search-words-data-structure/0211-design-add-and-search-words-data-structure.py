class TrieNode:
    def __init__(self, ch):
        self.data = ch
        self.children = [None] * 26
        self.is_terminal = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode("")

    def insert_util(self, root, word):
        if len(word) == 0:
            root.is_terminal = True
            return
        
        index = ord(word[0]) - ord('a')

        if root.children[index]:
            child = root.children[index]
        else:
            child = TrieNode(word[0])
            root.children[index] = child
        
        self.insert_util(child, word[1:])

    def addWord(self, word: str) -> None:
        self.insert_util(self.root, word)

    def search_util(self, root, word):

        if len(word) == 0:
            return root.is_terminal
        
        if word[0] == '.':
            for child in root.children:
                if child and self.search_util(child, word[1:]):
                    return True
            return False
        else:
            index = ord(word[0]) - ord('a')

            if root.children[index]:
                child = root.children[index]
            else:
                return False
            
            return self.search_util(child, word[1:])

    def search(self, word: str) -> bool:
        return self.search_util(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

'''
    def search_util(self, root, word):
        if len(word) == 0:
            return root.is_terminal
        
        index = ord(word[0]) - ord('a')

        if root.children[index]:
            child = root.children[index]
        else:
            return False
        
        return self.search_util(child, word[1:])
    
    def search(self, word: str) -> bool:
        return self.search_util(self.root, word)
'''