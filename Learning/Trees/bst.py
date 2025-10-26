class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None  

class BinarySearchTree:
    def __init__(self, value):
        self.root = None

    def insert(self,value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True
        else:
            temp = self.root
            while True:
                if new_node.value == temp.value:
                    return False
                if new_node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        return True
                    temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp:
            if value < temp.value:  # Fixed incorrect condition
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False  # Return False if value is not found


# Test cases
if __name__ == "__main__":
    bst = BinarySearchTree(None)

    # Test inserting into an empty tree
    assert bst.insert(10) == True  # Root node
    assert bst.root.value == 10

    # Test inserting smaller value (left child)
    assert bst.insert(5) == True
    assert bst.root.left.value == 5

    # Test inserting larger value (right child)
    assert bst.insert(15) == True
    assert bst.root.right.value == 15

    # Test inserting duplicate value
    assert bst.insert(10) == False  # Duplicate value not allowed

    # Test inserting deeper nodes
    assert bst.insert(3) == True
    assert bst.root.left.left.value == 3
    assert bst.insert(7) == True
    assert bst.root.left.right.value == 7

    # Test cases for contains method
    assert bst.contains(10) == True  # Root node exists
    assert bst.contains(5) == True   # Left child exists
    assert bst.contains(15) == True  # Right child exists
    assert bst.contains(3) == True   # Deeper left node exists
    assert bst.contains(7) == True   # Deeper right node exists
    assert bst.contains(20) == False # Non-existent value
    assert bst.contains(0) == False  # Non-existent value

    print("All test cases passed!")
    print("All test cases passed for contains method!")