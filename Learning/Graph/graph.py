class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v2].append(v1)
            self.adj_list[v1].append(v2)
            return True
        return False

    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            if v2 in self.adj_list[v1]:
                self.adj_list[v1].remove(v2)
            if v1 in self.adj_list[v2]:
                self.adj_list[v2].remove(v1)
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in list(self.adj_list[vertex]):
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

# Test cases (assert-based)
if __name__ == "__main__":
    graph = Graph()

    # add_vertex
    assert graph.add_vertex("A") is True
    assert graph.add_vertex("B") is True
    assert graph.add_vertex("A") is False  # duplicate

    # add_edge (idempotent)
    assert graph.add_edge("A", "B") is True
    assert graph.add_edge("A", "B") is True  # second call succeeds but does not duplicate
    assert graph.adj_list == {"A": ["B"], "B": ["A"]}

    # remove_edge
    assert graph.remove_edge("A", "B") is True
    assert graph.remove_edge("A", "C") is False  # C does not exist
    assert graph.adj_list == {"A": [], "B": []}

    # remove_vertex
    assert graph.add_vertex("C") is True
    assert graph.add_edge("A", "C") is True
    assert graph.remove_vertex("C") is True
    assert "C" not in graph.adj_list
    assert "C" not in graph.adj_list.get("A", [])

    print("All tests passed.")
