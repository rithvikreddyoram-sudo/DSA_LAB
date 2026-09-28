class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def delete(self, key):
        temp = self.head
        if temp is not None and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            print("Value", key, "not found")
            return
        prev.next = temp.next

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_end(10)
    sll.insert_at_end(20)
    sll.insert_at_end(30)
    sll.insert_at_beginning(5)
    print("Linked list:")
    sll.display()
    sll.delete(20)
    print("After deleting 20:")
    sll.display()
    sll.delete(99)
