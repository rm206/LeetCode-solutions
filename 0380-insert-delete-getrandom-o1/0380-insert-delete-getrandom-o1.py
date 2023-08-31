import random
class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        else:
            self.arr.append(val)
            self.map[val] = len(self.arr) - 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.map:
            last_elt = self.arr[-1]
            remove_index = self.map[val]
            
            self.map[last_elt] = remove_index
            self.arr[remove_index] = last_elt
            
            self.arr[-1] = val
            self.arr.pop()
            self.map.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()