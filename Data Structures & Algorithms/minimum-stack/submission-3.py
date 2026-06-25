class MinStack:

    def __init__(self):
        self.stack = []
        self.minin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minin) == 0:
            self.minin.append(val)
        elif (self.stack[-1] <= self.minin[-1]):
            self.minin.append(self.stack[-1])
        

    def pop(self) -> None:
        if self.stack[-1] == self.minin[-1]:
            self.minin.pop(-1)
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minin[-1]
        
