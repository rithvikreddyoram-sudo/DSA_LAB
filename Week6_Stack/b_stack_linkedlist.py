class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        print(value, "pushed")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
        else:
            removed = self.top
            self.top = self.top.next
            print(removed.data, "popped")

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            temp = self.top
            print("Stack (top to bottom):", end=" ")
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.display()
    s.peek()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
