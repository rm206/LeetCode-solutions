class MyStack:

    def __init__(self):
        self.q = []
        self.len = 0

    def push(self, x: int) -> None:
        self.q.append(x)
        self.len += 1

    def pop(self) -> int:
        for ctr in range(self.len):
            if ctr == self.len - 1:
                val = self.q.pop(0)
                self.len -= 1
            else:
                self.q.append(self.q.pop(0))
        
        return val

    def top(self) -> int:
        for ctr in range(self.len):
            if ctr == self.len - 1:
                val = self.q.pop(0)
                self.q.append(val)
            else:
                self.q.append(self.q.pop(0))
        
        return val

    def empty(self) -> bool:
        return self.len == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()