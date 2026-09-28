class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def delete(self, key):
        temp = self.head
        while temp is not None and temp.data != key:
            temp = temp.next
        if temp is None:
            print("Value", key, "not found")
            return
        if temp.prev is not None:
            temp.prev.next = temp.next
        else:
            self.head = temp.next
        if temp.next is not None:
            temp.next.prev = temp.prev

    def display_forward(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def display_backward(self):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    dll.insert_at_beginning(5)
    print("Forward:")
    dll.display_forward()
    print("Backward:")
    dll.display_backward()
    dll.delete(20)
    print("After deleting 20:")
    dll.display_forward()
