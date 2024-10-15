class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next  # Pointer to the next node in the linked list

    def get_data(self):
        return self.data  # Return the data of the node

    def get_next(self):
        return self.next  # Return the next node

    def set_data(self, data):
        self.data = data  # Set the data of the node

    def set_next(self, next):
        self.next = next  # Set the next node


class LinkedList:
    def __init__(self, root=None):
        self.root = root  # Initialize the linked list with an optional root node
        self.size = 0  # Keep track of the size of the linked list

    def __str__(self):
        string = ""
        current_node = self.root
        while current_node:
            string += f"{current_node.data} -> "  # Append node's data to the string
            current_node = current_node.get_next()  # Move to the next node
        string += "None"  # Indicate the end of the list
        return string  # Return the string representation of the linked list

    def is_empty(self):
        return self.size == 0  # Return True if the linked list is empty

    def get_size(self):
        return self.size  # Return the size of the linked list

    def add(self, data, position: int = None):

        if position is not None and position > self.size:
            raise IndexError("Index out of bound.")  # Raise error if position is invalid

        new_node = Node(data)  # Create a new node with the given data
        if self.is_empty() or position is None or position == 0:
            new_node.set_next(self.root)  # Insert new node at the head
            self.root = new_node  # Update the root to point to the new node
            self.size += 1  # Increase size of the list
            return

        else:
            current_node = self.root
            position_count = 0

            while position_count < position - 1 and current_node.get_next() is not None:
                current_node = current_node.get_next()  # Traverse to the desired position
                position_count += 1

            new_node.set_next(current_node.get_next())  # Link the new node to the next node
            current_node.set_next(new_node)  # Link the previous node to the new node
        self.size += 1  # Increase size of the list

    def remove(self, data=None):

        # Handle empty linked list
        if not self.root:
            return False

        previous_node = None
        current_node = self.root

        # If the root node is the one to be removed
        if current_node.get_data() == data:
            self.root = self.root.get_next()  # Update the root to the next node
            self.size -= 1  # Decrease size of the list
            return True

        while current_node:
            if current_node.get_data() == data:
                if previous_node:
                    previous_node.set_next(current_node.get_next())  # Bypass the current node
                self.size -= 1  # Decrease size of the list
                return True
            previous_node = current_node  # Keep track of the previous node
            current_node = current_node.get_next()  # Move to the next node

    def find(self, data):
        current_node = self.root

        while current_node:
            if current_node.get_data() == data:
                return data  # Return data if found
            current_node = current_node.get_next()  # Continue searching
        return None  # Return None if the data is not found

    def append(self, data):
        new_node = Node(data)  # Create a new node

        if self.is_empty():
            self.root = new_node  # If the list is empty, set the new node as root

        else:
            current_node = self.root
            while current_node.get_next():
                current_node = current_node.get_next()  # Traverse to the end of the list
            current_node.set_next(new_node)  # Add new node at the end
        self.size += 1  # Increase size of the list

    def reverse(self):
        previous_node = None
        current_node = self.root

        while current_node:
            next_node = current_node.get_next()  # Store the next node
            current_node.set_next(previous_node)  # Reverse the link
            previous_node = current_node  # Move previous_node forward
            current_node = next_node  # Move current_node forward

        self.root = previous_node  # Update the root to the last node (new head)

    def clear(self):
        self.size = 0
        self.root = None  # Clear the linked list by resetting the root and size

    def print_all(self):
        current_node = self.root
        while current_node:
            print(current_node.get_data())  # Print the data of each node
            current_node = current_node.get_next()  # Move to the next node


# Example usage
linked_list = LinkedList()
linked_list.add(10)  # Add 10 to the linked list
linked_list.add(20)  # Add 20 to the linked list
linked_list.add(30)  # Add 30 to the linked list
linked_list.add(40)  # Add 40 to the linked list

print(linked_list.find(20))  # Find 20 in the linked list
print(linked_list.find(100))  # Try to find 100 (not in the list)

print("-------")
linked_list.append(10000)  # Append 10000 to the end of the linked list
linked_list.add(222, 4)  # Add 222 at position 4

linked_list.print_all()  # Print all the elements in the list
print(linked_list.size)  # Print the size of the list

linked_list.reverse()  # Reverse the linked list
print(linked_list)  # Print the reversed linked list
