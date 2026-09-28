class Stack:
    def __init__(self, size):
        self.size = size
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.size

    def push(self, value):
        if self.is_full():
            print("Stack Overflow")
        else:
            self.items.append(value)
            print(value, "pushed")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
        else:
            print(self.items.pop(), "popped")

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Top element:", self.items[-1])

    def display(self):
        print("Stack (bottom to top):", self.items)


if __name__ == "__main__":
    s = Stack(3)
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.display()
    s.peek()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
