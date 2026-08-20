# Min Stack

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


# Example Usage
s = MinStack()

s.push(5)
s.push(2)
s.push(8)
s.push(1)

print(s.getMin())  # 1
s.pop()
print(s.getMin())  # 2
print(s.top())     # 8
