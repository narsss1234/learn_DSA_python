class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_Queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
            self.length = 1
            return True
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1
            return True
        
    def dequeue(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.first
            self.first = None
            self.last = None
            self.length = 0
            return temp.value
        else:
            temp = self.first

            self.first = self.first.next
            temp.next = None
            self.length -= 1
            return temp.value

         

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1 

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
            self.height = 1
            return True
        else:
            new_node.next = self.top
            self.top = new_node
            self.height += 1   
            return True

    def pop(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next  # Fix: Update top before breaking the link
            temp.next = None
            self.height -= 1
            return temp.value

# Test cases
if __name__ == "__main__":
    # Test Stack initialization
    stack = Stack(10)
    print("Initial stack:")
    stack.print_stack()  # Expected output: 10

    # Test push method
    stack.push(20)
    print("\nStack after pushing 20:")
    stack.print_stack()  # Expected output: 20, 10

    # Test stack height
    print("\nStack height:", stack.height)  # Expected output: 2

    # Test pop method
    popped_value = stack.pop()
    print("\nPopped value:", popped_value)  # Expected output: 20
    print("Stack after popping:")
    stack.print_stack()  # Expected output: 10
    print("\nStack height:", stack.height)  # Expected output: 1

    # Test Queue initialization
    queue = Queue(10)
    print("\nInitial queue:")
    queue.print_Queue()  # Expected output: 10

    # Test enqueue method
    queue.enqueue(20)
    print("\nQueue after enqueueing 20:")
    queue.print_Queue()  # Expected output: 20, 10

    # Test queue length
    print("\nQueue length:", queue.length)  # Expected output: 2

    # Test dequeue method
    dequeued_value = queue.dequeue()
    print("\nDequeued value:", dequeued_value)  # Expected output: 10
    print("Queue after dequeueing:")
    queue.print_Queue()  # Expected output: 20
    print("\nQueue length:", queue.length)  # Expected output: 1

    dequeued_value = queue.dequeue()
    print("\nDequeued value:", dequeued_value)  # Expected output: 20
    print("Queue after dequeueing:")
    queue.print_Queue()  # Expected output: (empty)
    print("\nQueue length:", queue.length)  # Expected output: 0

    # Test dequeue on empty queue
    dequeued_value = queue.dequeue()
    print("\nDequeued value from empty queue:", dequeued_value)  # Expected output: None