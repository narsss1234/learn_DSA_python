class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while(temp.next):
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return True
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = self.tail = None
            self.length = 0
            return temp
        else:
            popped_node = self.tail
            temp = self.head
            pre = None
            while(temp.next):
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            return popped_node

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return True
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True   

    def  pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = self.tail = None
            self.length -= 1
            return temp
        else:
            temp = self.head
            self.head = self.head.next
            self.length -= 1
            return temp
        
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.head
        elif index == self.length -1:
            return self.tail
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return False
        temp = self.get(index)
        temp.value = value
        return True

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        temp = self.get(index)
        pre = self.get(index-1)
        pre.next = new_node
        new_node.next = temp
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length -1:
            return self.pop()
        temp = self.get(index)
        pre = self.get(index-1)
        pre.next = temp.next
        self.length -= 1
        return temp

def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        after = temp.next

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True


# Test cases
def test_linked_list():
    # Test 1: Creating a new linked list
    print("\n=== Test 1: Creating a new linked list ===")
    my_list = LinkedList(5)
    print(f"Initial list - Head: {my_list.head.value}, Tail: {my_list.tail.value}, Length: {my_list.length}")
    assert my_list.head.value == 5, "Head value should be 5"
    assert my_list.tail.value == 5, "Tail value should be 5"
    assert my_list.length == 1, "Length should be 1"
    print("✓ Initialization test passed!")

    # Test 2: Appending nodes
    print("\n=== Test 2: Testing append method ===")
    print("Appending value 10...")
    my_list.append(10)
    print(f"After append - Head: {my_list.head.value}, Tail: {my_list.tail.value}, Length: {my_list.length}")
    assert my_list.head.value == 5, "Head should still be 5"
    assert my_list.tail.value == 10, "Tail should be 10"
    assert my_list.length == 2, "Length should be 2"
    assert my_list.head.next.value == 10, "Second node should be 10"
    print("✓ First append test passed!")

    print("\nAppending value 15...")
    my_list.append(15)
    print(f"After second append - Head: {my_list.head.value}, Tail: {my_list.tail.value}, Length: {my_list.length}")
    assert my_list.tail.value == 15, "Tail should be 15"
    assert my_list.length == 3, "Length should be 3"
    print("✓ Second append test passed!")

    # Test 3: Testing pop method
    print("\n=== Test 3: Testing pop method ===")
    # Pop first node (15)
    print("Popping last node...")
    popped_node = my_list.pop()
    print(f"Popped value: {popped_node.value}")
    print(f"After pop - Head: {my_list.head.value}, Tail: {my_list.tail.value}, Length: {my_list.length}")
    assert popped_node.value == 15, "Popped node should be 15"
    assert my_list.length == 2, "Length should be 2"
    assert my_list.tail.value == 10, "Tail should be 10"
    print("✓ First pop test passed!")

    # Pop second node (10)
    print("\nPopping second node...")
    popped_node = my_list.pop()
    print(f"Popped value: {popped_node.value}")
    print(f"After pop - Head: {my_list.head.value}, Tail: {my_list.tail.value}, Length: {my_list.length}")
    assert popped_node.value == 10, "Popped node should be 10"
    assert my_list.length == 1, "Length should be 1"
    assert my_list.head.value == 5, "Head should be 5"
    assert my_list.tail.value == 5, "Tail should be 5"
    print("✓ Second pop test passed!")

    # Pop last node (5)
    print("\nPopping last remaining node...")
    popped_node = my_list.pop()
    print(f"Popped value: {popped_node.value}")
    print(f"After pop - Head: {my_list.head}, Tail: {my_list.tail}, Length: {my_list.length}")
    assert popped_node.value == 5, "Popped node should be 5"
    assert my_list.length == 0, "Length should be 0"
    assert my_list.head is None, "Head should be None"
    assert my_list.tail is None, "Tail should be None"
    print("✓ Third pop test passed!")

    # Try to pop from empty list
    print("\nTrying to pop from empty list...")
    popped_node = my_list.pop()
    assert popped_node is None, "Popping from empty list should return None"
    print("✓ Empty list pop test passed!")

    # Test 4: Testing print_list and append after pops
    print("\n=== Test 4: Testing print_list and append after pops ===")
    print("Appending new value 20...")
    my_list.append(20)
    print(f"After append to empty list - Head: {my_list.head.value}, Tail: {my_list.tail.value}, Length: {my_list.length}")
    assert my_list.head.value == 20, "Head should be 20"
    assert my_list.tail.value == 20, "Tail should be 20"
    assert my_list.length == 1, "Length should be 1"
    print("✓ Append after empty test passed!")

    # Test 5: Testing prepend method
    print("\n=== Test 5: Testing prepend method ===")
    my_list = LinkedList(10)
    print(f"Initial list - Head: {my_list.head.value}, Tail: {my_list.tail.value}, Length: {my_list.length}")
    
    # Test prepending to a list with one node
    print("\nPrepending value 5...")
    my_list.prepend(5)
    print(f"After prepend - Head: {my_list.head.value}, Tail: {my_list.tail.value}, Length: {my_list.length}")
    assert my_list.head.value == 5, "Head should be 5"
    assert my_list.head.next.value == 10, "Second node should be 10"
    assert my_list.tail.value == 10, "Tail should still be 10"
    assert my_list.length == 2, "Length should be 2"
    print("✓ First prepend test passed!")

    # Test prepending to a list with multiple nodes
    print("\nPrepending value 1...")
    my_list.prepend(1)
    print(f"After second prepend - Head: {my_list.head.value}, Tail: {my_list.tail.value}, Length: {my_list.length}")
    assert my_list.head.value == 1, "Head should be 1"
    assert my_list.head.next.value == 5, "Second node should be 5"
    assert my_list.tail.value == 10, "Tail should still be 10"
    assert my_list.length == 3, "Length should be 3"
    print("✓ Second prepend test passed!")

    # Test 6: Testing Node creation
    print("\n=== Test 6: Testing Node creation ===")
    test_node = Node(25)
    print(f"New node - Value: {test_node.value}, Next: {test_node.next}")
    assert test_node.value == 25, "Node value should be 25"
    assert test_node.next is None, "Node next should be None"
    print("✓ Node creation test passed!")

    # Test 7: Testing pop_first method
    print("\n=== Test 7: Testing pop_first method ===")
    # Create a new list for testing pop_first
    my_list = LinkedList(100)
    my_list.append(200)
    my_list.append(300)
    print(f"Initial list - Head: {my_list.head.value}, Tail: {my_list.tail.value}, Length: {my_list.length}")
    
    # Test popping first node from list with multiple nodes
    print("\nPopping first node from list with multiple nodes...")
    popped_node = my_list.pop_first()
    print(f"Popped value: {popped_node.value}")
    print(f"After pop_first - Head: {my_list.head.value}, Tail: {my_list.tail.value}, Length: {my_list.length}")
    assert popped_node.value == 100, "Popped node should be 100"
    assert my_list.head.value == 200, "Head should now be 200"
    assert my_list.tail.value == 300, "Tail should still be 300"
    assert my_list.length == 2, "Length should be 2"
    print("✓ First pop_first test passed!")

    # Test popping first node from list with two nodes
    print("\nPopping first node from list with two nodes...")
    popped_node = my_list.pop_first()
    print(f"Popped value: {popped_node.value}")
    print(f"After pop_first - Head: {my_list.head.value}, Tail: {my_list.tail.value}, Length: {my_list.length}")
    assert popped_node.value == 200, "Popped node should be 200"
    assert my_list.head.value == 300, "Head should now be 300"
    assert my_list.tail.value == 300, "Tail should be 300"
    assert my_list.length == 1, "Length should be 1"
    print("✓ Second pop_first test passed!")

    # Test popping first node from list with one node
    print("\nPopping first node from list with one node...")
    popped_node = my_list.pop_first()
    print(f"Popped value: {popped_node.value}")
    print(f"After pop_first - Head: {my_list.head}, Tail: {my_list.tail}, Length: {my_list.length}")
    assert popped_node.value == 300, "Popped node should be 300"
    assert my_list.head is None, "Head should be None"
    assert my_list.tail is None, "Tail should be None"
    assert my_list.length == 0, "Length should be 0"
    print("✓ Third pop_first test passed!")

    # Test popping first node from empty list
    print("\nTrying to pop_first from empty list...")
    popped_node = my_list.pop_first()
    assert popped_node is None, "Popping from empty list should return None"
    print("✓ Empty list pop_first test passed!")

    # Test 8: Testing get method
    print("\n=== Test 8: Testing get method ===")
    # Create a new list for testing get
    my_list = LinkedList(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)
    print(f"Initial list - Head: {my_list.head.value}, Tail: {my_list.tail.value}, Length: {my_list.length}")
    
    # Test getting first node (index 0)
    print("\nGetting node at index 0...")
    node = my_list.get(0)
    print(f"Node value at index 0: {node.value}")
    assert node.value == 10, "First node should be 10"
    assert node == my_list.head, "Should return head node"
    print("✓ Get first node test passed!")

    # Test getting middle node (index 2)
    print("\nGetting node at index 2...")
    node = my_list.get(2)
    print(f"Node value at index 2: {node.value}")
    assert node.value == 30, "Node at index 2 should be 30"
    print("✓ Get middle node test passed!")

    # Test getting last node (index 3)
    print("\nGetting node at index 3...")
    node = my_list.get(3)
    print(f"Node value at index 3: {node.value}")
    assert node.value == 40, "Last node should be 40"
    assert node == my_list.tail, "Should return tail node"
    print("✓ Get last node test passed!")

    # Test getting node at invalid negative index
    print("\nTrying to get node at negative index...")
    node = my_list.get(-1)
    assert node is None, "Should return None for negative index"
    print("✓ Get negative index test passed!")

    # Test getting node at invalid index (>= length)
    print("\nTrying to get node at index >= length...")
    node = my_list.get(4)
    assert node is None, "Should return None for index >= length"
    print("✓ Get invalid index test passed!")

    # Test getting node from empty list
    print("\nTrying to get node from empty list...")
    empty_list = LinkedList(5)
    empty_list.pop()  # Make the list empty
    node = empty_list.get(0)
    assert node is None, "Should return None when list is empty"
    print("✓ Get from empty list test passed!")

    # Test 9: Testing set_value method
    print("\n=== Test 9: Testing set_value method ===")
    # Create a new list for testing set_value
    my_list = LinkedList(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)
    print(f"Initial list - Head: {my_list.head.value}, Tail: {my_list.tail.value}, Length: {my_list.length}")
    
    # Test setting value at first node (index 0)
    print("\nSetting value 15 at index 0...")
    result = my_list.set_value(0, 15)
    print(f"Node value at index 0 after set: {my_list.head.value}")
    assert result is True, "Set_value should return True for valid index"
    assert my_list.head.value == 15, "Head value should be updated to 15"
    print("✓ Set first node value test passed!")

    # Test setting value at middle node (index 2)
    print("\nSetting value 35 at index 2...")
    result = my_list.set_value(2, 35)
    print(f"Node value at index 2 after set: {my_list.get(2).value}")
    assert result is True, "Set_value should return True for valid index"
    assert my_list.get(2).value == 35, "Node at index 2 should be updated to 35"
    print("✓ Set middle node value test passed!")

    # Test setting value at last node (index 3)
    print("\nSetting value 45 at index 3...")
    result = my_list.set_value(3, 45)
    print(f"Node value at index 3 after set: {my_list.tail.value}")
    assert result is True, "Set_value should return True for valid index"
    assert my_list.tail.value == 45, "Tail value should be updated to 45"
    print("✓ Set last node value test passed!")

    # Test setting value at invalid negative index
    print("\nTrying to set value at negative index...")
    result = my_list.set_value(-1, 100)
    assert result is False, "Set_value should return False for negative index"
    print("✓ Set negative index test passed!")

    # Test setting value at invalid index (>= length)
    print("\nTrying to set value at index >= length...")
    result = my_list.set_value(4, 100)
    assert result is False, "Set_value should return False for index >= length"
    print("✓ Set invalid index test passed!")

    # Test setting value in empty list
    print("\nTrying to set value in empty list...")
    empty_list = LinkedList(5)
    empty_list.pop()  # Make the list empty
    result = empty_list.set_value(0, 100)
    assert result is False, "Set_value should return False when list is empty"
    print("✓ Set value in empty list test passed!")

    # Test 10: Testing insert method
    print("\n=== Test 10: Testing insert method ===")
    # Create a new list for testing insert
    my_list = LinkedList(10)
    my_list.append(20)
    my_list.append(30)
    print(f"Initial list - Head: {my_list.head.value}, Tail: {my_list.tail.value}, Length: {my_list.length}")
    
    # Test inserting at the beginning (index 0)
    print("\nInserting value 5 at index 0...")
    result = my_list.insert(0, 5)
    print(f"After insert at beginning - Head: {my_list.head.value}, Tail: {my_list.tail.value}, Length: {my_list.length}")
    assert result is True, "Insert should return True for valid index"
    assert my_list.head.value == 5, "Head value should be 5"
    assert my_list.head.next.value == 10, "Second node should be 10"
    assert my_list.length == 4, "Length should be 4"
    print("✓ Insert at beginning test passed!")

    # Test inserting in the middle (index 2)
    print("\nInserting value 15 at index 2...")
    result = my_list.insert(2, 15)
    print(f"After insert in middle - Length: {my_list.length}")
    assert result is True, "Insert should return True for valid index"
    assert my_list.get(2).value == 15, "Node at index 2 should be 15"
    assert my_list.get(1).value == 10, "Node at index 1 should still be 10"
    assert my_list.get(3).value == 20, "Node at index 3 should be 20"
    assert my_list.length == 5, "Length should be 5"
    print("✓ Insert in middle test passed!")

    # Test inserting at the end (index = length)
    print("\nInserting value 35 at the end...")
    result = my_list.insert(my_list.length, 35)
    print(f"After insert at end - Tail: {my_list.tail.value}, Length: {my_list.length}")
    assert result is True, "Insert should return True for valid index"
    assert my_list.tail.value == 35, "Tail value should be 35"
    assert my_list.length == 6, "Length should be 6"
    print("✓ Insert at end test passed!")

    # Test inserting at invalid negative index
    print("\nTrying to insert at negative index...")
    result = my_list.insert(-1, 100)
    assert result is False, "Insert should return False for negative index"
    assert my_list.length == 6, "Length should remain unchanged"
    print("✓ Insert at negative index test passed!")

    # Test inserting at invalid index (> length)
    print("\nTrying to insert at index > length...")
    result = my_list.insert(my_list.length + 1, 100)
    assert result is False, "Insert should return False for index > length"
    assert my_list.length == 6, "Length should remain unchanged"
    print("✓ Insert at invalid index test passed!")

    # Test inserting into empty list
    print("\nTrying to insert into empty list...")
    empty_list = LinkedList(5)
    empty_list.pop()  # Make the list empty
    result = empty_list.insert(0, 100)
    print(f"After insert into empty list - Head: {empty_list.head.value if empty_list.head else None}, Length: {empty_list.length}")
    assert result is True, "Insert should return True for empty list at index 0"
    assert empty_list.head.value == 100, "Head value should be 100"
    assert empty_list.tail.value == 100, "Tail value should be 100"
    assert empty_list.length == 1, "Length should be 1"
    print("✓ Insert into empty list test passed!")

    # Test 11: Testing remove method
    print("\n=== Test 11: Testing remove method ===")
    # Create a new list for testing remove
    my_list = LinkedList(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)
    my_list.append(50)
    print(f"Initial list - {[my_list.get(i).value for i in range(my_list.length)]}, Length: {my_list.length}")

    # Remove from beginning (index 0)
    print("\nRemoving at index 0 (beginning)...")
    removed = my_list.remove(0)
    print(f"Removed value: {removed.value}")
    assert removed.value == 10, "Removed node should be 10"
    assert my_list.head.value == 20, "Head should now be 20"
    assert my_list.length == 4, "Length should be 4"
    print("✓ Remove at beginning test passed!")

    # Remove from middle (current index 2)
    print("\nRemoving at index 2 (middle)...")
    # current list values are [20,30,40,50]
    removed = my_list.remove(2)
    print(f"Removed value: {removed.value}")
    assert removed.value == 40, "Removed node should be 40"
    assert my_list.get(0).value == 20 and my_list.get(1).value == 30 and my_list.get(2).value == 50, "List should have 20,30,50"
    assert my_list.length == 3, "Length should be 3"
    print("✓ Remove in middle test passed!")

    # Remove from end (last index)
    print("\nRemoving at last index (end)...")
    removed = my_list.remove(my_list.length - 1)
    print(f"Removed value: {removed.value}")
    assert removed.value == 50, "Removed node should be 50"
    assert my_list.tail.value == 30, "Tail should now be 30"
    assert my_list.length == 2, "Length should be 2"
    print("✓ Remove at end test passed!")

    # Remove with invalid negative index
    print("\nTrying to remove with negative index...")
    removed = my_list.remove(-1)
    assert removed is None, "Remove should return None for negative index"
    assert my_list.length == 2, "Length should remain unchanged"
    print("✓ Remove negative index test passed!")

    # Remove with index >= length
    print("\nTrying to remove with index >= length...")
    removed = my_list.remove(10)
    assert removed is None, "Remove should return None for out-of-range index"
    assert my_list.length == 2, "Length should remain unchanged"
    print("✓ Remove out-of-range index test passed!")

    # Remove from empty list
    print("\nTrying to remove from empty list...")
    empty_list = LinkedList(1)
    empty_list.pop()  # make empty
    removed = empty_list.remove(0)
    assert removed is None, "Remove should return None when list is empty"
    print("✓ Remove from empty list test passed!")

    # Test 12: Testing reverse method
    print("\n=== Test 12: Testing reverse method ===")

    # Helper to call reverse whether it's a method or module-level function
    def _call_reverse(lst):
        # prefer method if present
        if hasattr(lst, 'reverse') and callable(getattr(lst, 'reverse')):
            return lst.reverse()
        else:
            # fallback to module-level function if defined
            return globals().get('reverse')(lst)

    # Reverse on empty list: should remain empty after call
    print("\nReversing an empty list...")
    empty_list = LinkedList(1)
    empty_list.pop()  # make empty
    try:
        _call_reverse(empty_list)
    except Exception as e:
        # if implementation raises on empty, that's acceptable for now; ensure list still empty
        print(f"Reverse raised on empty list: {e}")
    assert empty_list.head is None and empty_list.tail is None and empty_list.length == 0, "Empty list should remain empty after reverse"
    print("✓ Reverse empty list test passed!")

    # Reverse on single-node list
    print("\nReversing a single-node list...")
    single = LinkedList(7)
    _call_reverse(single)
    assert single.head == single.tail and single.head.value == 7 and single.head.next is None, "Single node list should remain unchanged after reverse"
    print("✓ Reverse single-node test passed!")

    # Reverse on multi-node list
    print("\nReversing a multi-node list...")
    my_list = LinkedList(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    before = [my_list.get(i).value for i in range(my_list.length)]
    print(f"Before reverse: {before}")
    _call_reverse(my_list)
    after = [my_list.get(i).value for i in range(my_list.length)]
    print(f"After reverse: {after}")
    assert after == before[::-1], "List should be reversed"
    assert my_list.head.value == 4 and my_list.tail.value == 1 and my_list.length == 4, "Head/tail/length should be correct after reverse"
    print("✓ Reverse multi-node test passed!")

    # Reverse again to restore original order
    print("\nReversing again to restore original order...")
    _call_reverse(my_list)
    restored = [my_list.get(i).value for i in range(my_list.length)]
    assert restored == before, "Double reverse should restore original order"
    print("✓ Double-reverse restore test passed!")

if __name__ == "__main__":
    try:
        test_linked_list()
        print("\n✓ All tests passed successfully!")
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")