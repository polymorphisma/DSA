class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next


class LinkedList:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def add(self, data):
        node = Node(data, self.root)
        self.root = node
        self.size += 1

    def remove(self, data=None):
        if data is None:
            self.root = self.root.next
            self.size -= 1

    def print_all(self):
        current_node = self.root
        while (current_node):
            print(current_node.data)
            current_node = current_node.next


linked_list = LinkedList()
linked_list.add(10)
linked_list.add(20)
linked_list.add(30)
linked_list.add(40)

linked_list.print_all()
print(linked_list.size)

print('---------------------------------------')
linked_list.remove()
linked_list.print_all()
print(linked_list.size)
