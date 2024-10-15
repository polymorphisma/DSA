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

        # to handle empty linkedlist
        if not self.root:
            return False

        previous_node = None
        current_node = self.root

        # if root node is needed to be removed
        if current_node.get_data() == data:
            self.root = self.root.get_next()
            self.size -= 1
            return True

        while current_node:
            if current_node.get_data() == data:
                if previous_node:
                    previous_node.set_next(current_node.get_next())
                self.size -= 1
                return True
            previous_node = current_node
            current_node = current_node.get_next()

    def find(self, data):
        current_node = self.root

        while current_node:
            if current_node.get_data() == data:
                return data
            current_node = current_node.get_next()

        return False

    def print_all(self):
        current_node = self.root
        while current_node:
            print(current_node.get_data())
            current_node = current_node.get_next()


linked_list = LinkedList()
linked_list.add(10)
linked_list.add(20)
linked_list.add(30)
linked_list.add(40)

print(linked_list.find(20))
print(linked_list.find(100))