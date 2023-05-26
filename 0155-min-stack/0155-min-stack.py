class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value_stack = []
        self.top_index = -1

    def push(self, val: int) -> None:
        if self.top_index == -1:
            self.min_value_stack.append(val)
        else:
            min_to_push = min(self.min_value_stack[self.top_index], val)
            self.min_value_stack.append(min_to_push)
        
        self.stack.append(val)
        self.top_index += 1       

    def pop(self) -> None:
        self.top_index -= 1
        self.stack.pop()
        self.min_value_stack.pop()

    def top(self) -> int:
        return self.stack[self.top_index]

    def getMin(self) -> int:
        return self.min_value_stack[self.top_index]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()