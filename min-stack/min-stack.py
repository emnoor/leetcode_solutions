class MinStack:

    def __init__(self):
        self._values = []
        self._min = None

    def push(self, val: int) -> None:
        self._values.append(val)
        self._min = None

    def pop(self) -> None:
        self._values.pop()
        self._min = None
        
    def top(self) -> int:
        return self._values[-1]
    
    def getMin(self) -> int:
        if self._min is None:
            self._min = min(self._values)
        return self._min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()