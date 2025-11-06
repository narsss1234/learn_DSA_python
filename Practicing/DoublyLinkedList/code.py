class Node:
    def __init__(self, value):
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
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
        

    def reverse(self):  
        
        if self.head is None or self.head.next:
            return 
        
        d = Node(0)
        
        d.next = self.head
        
        self.head.prev = d
        
        dummy = d
        
        temp = self.head
        
        while(temp and temp.next):
            to_move = temp.next
            
            temp.next = to_move.next
            dummy.next.prev = to_move
            
            to_move.next = dummy.next
            
            dummy.next = to_move
             
            to_move.prev = dummy
             
        self.head = d.next
        self.head.prev = None
        temp = self.head
        self.head = self.tail
        self.tail = temp
        




my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)


print('DLL before reverse():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.reverse()


print('\nDLL after reverse():')
my_doubly_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    DLL before reverse():
    1 <-> 2 <-> 3 <-> 4 <-> 5
    
    DLL after reverse():
    5 <-> 4 <-> 3 <-> 2 <-> 1

"""

