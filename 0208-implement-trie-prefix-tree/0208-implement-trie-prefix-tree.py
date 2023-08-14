class TrieNode:
    def __init__(self, ch):
        self.data = ch
        self.children = [None for i in range(26)]
        self.end = False
    
class Trie:

    def __init__(self):
        self.root = TrieNode("")

    def insert_util(self, root, word):
        if len(word) == 0:
            root.end = True
            return
    
        index = ord(word[0]) - ord('a')
        
        if root.children[index]:
            child = root.children[index]
        else:
            child = TrieNode(word[0])
            root.children[index] = child
        
        self.insert_util(child, word[1 : ])
    
    def insert(self, word: str) -> None:
        self.insert_util(self.root, word)

    def search_util(self, root, word):
        if len(word) == 0:
            return root.end == True
        
        index = ord(word[0]) - ord('a')
        
        if root.children[index]:
            child = root.children[index]
            return self.search_util(child, word[1 : ])
        else:
            return False
    
    def search(self, word: str) -> bool:
        return self.search_util(self.root, word)

    def prefix_util(self, root, prefix):
        if len(prefix) == 0:
            return True
        
        index = ord(prefix[0]) - ord('a')
        
        if root.children[index]:
            child = root.children[index]
            return self.prefix_util(child, prefix[1 : ])
        else:
            return False    
    
    def startsWith(self, prefix: str) -> bool:
        return self.prefix_util(self.root, prefix)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)