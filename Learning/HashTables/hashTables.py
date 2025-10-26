class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, " :", val)

    def set_item(self, key, value):
        index = self.__hash(key)

        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for item in self.data_map:
            if item is not None:
                for i in range(len(item)):
                    all_keys.append(item[i][0])
        return all_keys

# Test cases
if __name__ == "__main__":
    ht = HashTable()

    # Test __hash method
    print("Testing __hash method:")
    print(ht._HashTable__hash("test"))  # Example hash value for "test"

    # Test print_table method
    print("\nTesting print_table method:")
    ht.print_table()  # Should print the empty hash table

    # Test set_item method
    print("\nTesting set_item method:")
    ht.set_item("key1", "value1")
    ht.set_item("key2", "value2")

    # Test get_item method
    print("\nTesting get_item method:")
    print(ht.get_item("key1"))  # Should print "value1"
    print(ht.get_item("key2"))  # Should print "value2"
    print(ht.get_item("key3"))  # Should print None (key does not exist)

    # Test collision handling
    print("\nTesting collision handling:")
    ht.set_item("key1", "new_value1")  # Update value for "key1"
    ht.set_item("key3", "value3")      # Add a new key that may collide
    print(ht.get_item("key1"))  # Should print "new_value1"
    print(ht.get_item("key3"))  # Should print "value3"

    # Test print_table after updates
    print("\nTesting print_table after updates:")
    ht.print_table()

    # Test keys method
    print("\nTesting keys method:")
    print(ht.keys())  # Should print all keys