class MinStack:

    def __init__(self):
        self.main_stack = []
        self.mins_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)

        if not self.mins_stack:
            self.mins_stack.append(val)
        else:
            self.mins_stack.append(min(val, self.mins_stack[-1]))

    def pop(self) -> None:
        self.main_stack.pop()
        self.mins_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.mins_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()