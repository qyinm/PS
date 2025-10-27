class MinStack:
    
    def __init__(self):
        self.st = []  

    def push(self, val: int) -> None:
        if not self.st:
            self.st.append((val, val))
        else:
            current_min = min(val, self.st[-1][1])
            self.st.append((val, current_min))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]