class Heap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index-1) // 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while(current > 0 and self.heap[current] > self.heap[self._parent(current)]):
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.headp.pop()
        max_value = self.heap[0]

        self.heap = self.heap.pop()
        self._sink_down(0)
        return max_value

    def sink_down():
        return True

# Test the Heap implementation
if __name__ == "__main__":
    # Create a new heap
    heap = Heap()
    
    print("Inserting values: 5, 3, 7, 1, 4, 6, 2")
    
    # Insert values one by one and print the heap after each insertion
    values = [5, 3, 7, 1, 4, 6, 2]
    for value in values:
        heap.insert(value)
        print(f"After inserting {value}: {heap.heap}")
    
    print("\nFinal heap structure:", heap.heap)
    print("Root (maximum) value:", heap.heap[0])