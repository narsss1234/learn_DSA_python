class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return True
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1
            return True

    def pop(self):
        if self.head is None:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return temp
    
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return True
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return True
    
    def pop_first(self):
        if self.head is None:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return temp
        
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head

            for i in range(self.length):
                if i == index:
                    return temp
                temp = temp.next

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return False
        elif index == 0:
            self.head.value = value
            return True
        elif index == self.length-1:
            self.tail.value = value
            return True
        else:
            temp = self.get(index)
            temp.value = value
            return True

    def insert(self, index, value):
        if index < 0 or index > self.length:  # Allow index == self.length for appending
            return False
        elif index == 0:
            self.prepend(value)
            return True
        elif index == self.length:  # Correct condition for appending
            self.append(value)
            return True
        else:
            new_node = Node(value)
            temp = self.get(index)
            pre = temp.prev
            
            temp.prev = new_node
            pre.next  = new_node
            new_node.prev  = pre
            new_node.next = temp
            self.length += 1
            return True
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            temp = self.get(index)
            pre = temp.prev
            post = temp.next
            pre.next = post
            post.prev = pre
            temp.next = temp.prev = None
            self.length -= 1
            return temp






# Test case for append
dll = DoublyLinkedList(10)
dll.append(20)
dll.append(30)
print("Test append:")
dll.print_list()  # Expected output: 10, 20, 30

# Test case for pop
print("\nTest pop:")
dll.pop()
dll.print_list()  # Expected output: 10, 20

# Test case for prepend
print("\nTest prepend:")
dll.prepend(5)
dll.print_list()  # Expected output: 5, 10, 20

# Test case for pop_first
print("\nTest pop_first:")
dll.pop_first()
dll.print_list()  # Expected output: 10, 20

# Test case for get
print("\nTest get:")
node = dll.get(1)
print(node.value if node else "Index out of range")  # Expected output: 20

# Test case for edge cases:
print("\nTest edge cases:")
dll.pop()
dll.pop()
dll.pop()  # Popping from an empty list
dll.print_list()  # Expected output: (no output, list is empty)

# Test case for set_value
print("\nTest set_value:")
dll = DoublyLinkedList(10)
dll.append(20)
dll.append(30)

dll.set_value(1, 25)  # Update value at index 1
dll.print_list()  # Expected output: 10, 25, 30

dll.set_value(0, 5)  # Update value at index 0
dll.print_list()  # Expected output: 5, 25, 30

dll.set_value(2, 35)  # Update value at index 2
dll.print_list()  # Expected output: 5, 25, 35

result = dll.set_value(3, 40)  # Attempt to update an out-of-range index
print(result)  # Expected output: False

# Test case for insert
print("\nTest insert:")
dll = DoublyLinkedList(10)
dll.append(20)
dll.append(30)

dll.insert(1, 15)  # Insert 15 at index 1
dll.print_list()  # Expected output: 10, 15, 20, 30

dll.insert(0, 5)  # Insert 5 at the head
dll.print_list()  # Expected output: 5, 10, 15, 20, 30

dll.insert(5, 35)  # Insert 35 at the tail
dll.print_list()  # Expected output: 5, 10, 15, 20, 30, 35

result = dll.insert(7, 40)  # Attempt to insert at an out-of-range index
print(result)  # Expected output: False

# Test case for remove
print("\nTest remove:")
dll = DoublyLinkedList(10)
dll.append(20)
dll.append(30)
dll.append(40)

dll.remove(1)  # Remove node at index 1
dll.print_list()  # Expected output: 10, 30, 40

dll.remove(0)  # Remove node at the head
dll.print_list()  # Expected output: 30, 40

dll.remove(1)  # Remove node at the tail
dll.print_list()  # Expected output: 30

result = dll.remove(5)  # Attempt to remove at an out-of-range index
print(result)  # Expected output: None

dll.remove(0)  # Remove the last remaining node
dll.print_list()  # Expected output: (no output, list is empty)