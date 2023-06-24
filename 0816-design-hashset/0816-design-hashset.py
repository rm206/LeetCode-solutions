class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.s = [None] * self.size

    def add(self, key: int) -> None:
        index = key % self.size

        if self.s[index] is None:
            self.s[index] = [key]
        else:
            if key in self.s[index]:
                return
            self.s[index].append(key)

    def remove(self, key: int) -> None:
        index = key % self.size

        if self.s[index] is not None:
            if key in self.s[index]:
                self.s[index].remove(key)

    def contains(self, key: int) -> bool:
        index = key % self.size

        if self.s[index] is None:
            return False
        else:
            return key in self.s[index]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)