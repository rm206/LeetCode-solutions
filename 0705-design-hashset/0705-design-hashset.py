class MyHashSet:

    def __init__(self):
        self.bins = 10
        self.store = [[] for _ in range(self.bins)]

    def add(self, key: int) -> None:
        if key not in self.store[key % self.bins]:
            self.store[key % self.bins].append(key)

    def remove(self, key: int) -> None:
        if key in self.store[key % self.bins]:
            self.store[key % self.bins].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.store[key % self.bins]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)