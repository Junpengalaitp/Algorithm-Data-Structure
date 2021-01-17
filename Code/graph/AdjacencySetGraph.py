from Code.graph.AbstractGraph import AbstractGraph


class AdjacencySetGraph(AbstractGraph):
    def __init__(self, num_vertices, directed=False):
        super().__init__(num_vertices, directed)
        self.vertex_list = [Node(i) for i in range(num_vertices)]

    def add_edge(self, v1, v2, weight=1):
        if self.is_out_of_bound(v1) or self.is_out_of_bound(v2):
            raise ValueError(f"vertices {v1} and {v2} are out of bounds")

        if weight != 1:
            raise ValueError("An edge cannot have weight differ than 1")

        self.vertex_list[v1].add_edge(v2)

        if not self.directed:
            self.vertex_list[v2].add_edge(v1)

    def get_adjacent_vertices(self, v):
        if self.is_out_of_bound(v):
            raise ValueError(f"cannot access vertex {v}")

        return self.vertex_list[v].get_adjacency_vertices()

    def get_indegree(self, v):
        if self.is_out_of_bound(v):
            raise ValueError(f"cannot access vertex {v}")
        return len([i for i in range(self.num_vertices) if v in self.get_adjacent_vertices(i)])

    def get_edge_weight(self, v1, v2):
        return 1

    def display(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                print(i, ": ", v)


class Node:
    def __init__(self, vertex_id) -> None:
        self.vertex_id = vertex_id
        self.adjacency_set = set()

    def add_edge(self, v):
        if self.vertex_id == v:
            raise ValueError(f"The vertex {v} can not be adjacent to itself")

        self.adjacency_set.add(v)

    def get_adjacency_vertices(self):
        return sorted(self.adjacency_set)


if __name__ == '__main__':
    g = AdjacencySetGraph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(2, 3)

    for i in range(4):
        print(f"{i} adjacent to: ", g.get_adjacent_vertices(i))

    for i in range(4):
        print(f"{i} indegree: ", g.get_indegree(i))

    for i in range(4):
        for j in g.get_adjacent_vertices(i):
            print(f"edge weight {i}, {j}, weight: {g.get_edge_weight(i, j)}")

    g.display()