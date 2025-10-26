# defining a Node class -> node will have a value, and also a next; bydefault next is none, later it can be changed
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

# defining a LinkedList class
class LinkedList:
    # LinkedList initialization function -> create a node, and then add a head and tail pointer, and also setting a lenght as 1
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    #Printing the linkedlist, temp will point to head first, later we can iterate for each next; when temp reaches none, it will stop
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Appending a new node to the end of the linkedlist; if there is no node; means length is zero, it will create one node and then point head and tail to it; else, tail.next is pointed to the new node and tail is the new node
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return popped_node
        else:
            temp = self.head
            pre = self.head
            while(temp.next):
                pre = temp
                temp = temp.next
            popped_node = temp
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            return popped_node
        
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return popped_node
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            self.length -= 1
            return popped_node

    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp  # Return the Node object instead of its value
    
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        new_node = Node(value)

        if index < 0 or index > self.length:
            return False
        elif index == self.length:  # Fix: Correct condition for appending at the end
            return self.append(value)
        elif index == 0:
            return self.prepend(value)
        else:
            temp = self.get(index - 1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        else:
            pre = self.get(index - 1)
            temp = pre.next
            pre.next = temp.next
            temp.next = None
            self.length -= 1
            return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

# Created a linked list with initial value 5
my_linked_list = LinkedList(5)

# Printing the type of the class of the linked list
print(type(my_linked_list))  # Expected: <class '__main__.LinkedList'>

# Printing the head pointer value
print(f"Head: {my_linked_list.head.value}")  # Expected: 5

# Printing the tail pointer value
print(f"Tail: {my_linked_list.tail.value}")  # Expected: 5

# Printing the next of tail pointer; it should be none
print(f"Tail.Next: {my_linked_list.tail.next}")  # Expected: None

# Printing the length of the linked list
print(f"Length of LinkedList: {my_linked_list.length}")  # Expected: 1

# Appending a new node to the linked list
my_linked_list.append(10)

# Printing the linked list
my_linked_list.print_list()  # Expected: 5, 10

# Printing the head pointer value
print(f"Head: {my_linked_list.head.value}")  # Expected: 5

# Printing the tail pointer value
print(f"Tail: {my_linked_list.tail.value}")  # Expected: 10

# Printing the next of tail pointer; it should be none
print(f"Tail.Next: {my_linked_list.tail.next}")  # Expected: None

# Printing the length of the linked list
print(f"Length of LinkedList: {my_linked_list.length}")  # Expected: 2

print("#Append #Append #Append #Append #Append #Append")
# Appending a new node to the linked list
my_linked_list.append(15)

# Printing the linked list
my_linked_list.print_list()  # Expected: 5, 10, 15

print("#Pop #Pop #Pop #Pop #Pop #Pop ")

# Popping the last node from the linked list
my_linked_list.pop()

# Printing the linked list
my_linked_list.print_list()  # Expected: 5, 10

print("#Prepend #Prepend #Prepend #Prepend #Prepend #Prepend ")

# Prepending a new node to the linked list
my_linked_list.prepend(0)

# Printing the linked list
my_linked_list.print_list()  # Expected: 0, 5, 10

print("#Pop_First #Pop_First #Pop_First #Pop_First #Pop_First #Pop_First #Pop_First ")

# Popping the first node from the linked list
my_linked_list.pop_first()

# Printing the linked list
my_linked_list.print_list()  # Expected: 5, 10

# Printing the value in the linked list based on index provided by user
print(f"Get index 0: {my_linked_list.get(0).value}")  # Expected: 5
print(f"Get index 1: {my_linked_list.get(1).value}")  # Expected: 10
print(f"Get index 2: {my_linked_list.get(2)}")  # Expected: None

print("set_value  set_value  set_value  set_value  set_value  set_value ")

# Changing the value in a certain index in the linked list
my_linked_list.set_value(0, 20)

# Printing the linked list
my_linked_list.print_list()  # Expected: 20, 10

print("Insert  Insert  Insert  Insert  Insert  Insert  Insert  Insert ")

# Using insert method to add a new node in a certain index
my_linked_list.insert(0, 30)
my_linked_list.insert(2, 40)

# Printing the linked list
my_linked_list.print_list()  # Expected: 30, 20, 40, 10

print("Remove  Remove  Remove  Remove  Remove  Remove  Remove  Remove ")

# Removing a node at a certain index
my_linked_list.remove(2)

# Printing the linked list
my_linked_list.print_list()  # Expected: 30, 20, 10

print("Reverse  Reverse  Reverse  Reverse  Reverse  Reverse  Reverse  Reverse ")

# Reversing the linked list
my_linked_list.reverse()

# Printing the linked list
my_linked_list.print_list()  # Expected: 10, 20, 30