class MinStack:

    def __init__(self):
        self.MinStack = []
        self.MainStack = []

    def push(self, val: int) -> None:
        self.MainStack.append(val)

        if not self.MinStack or val <= self.MinStack[-1]:
            self.MinStack.append(val)
        else:
            self.MinStack.append(self.MinStack[-1])


    def pop(self) -> None:
        self.MinStack.pop()
        self.MainStack.pop()

    def top(self) -> int:
        return self.MainStack[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]
        
