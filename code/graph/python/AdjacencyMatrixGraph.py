from graph.python.AbstractGraph import AbstractGraph


class AdjacencyMatrixGraph(AbstractGraph):
    def __init__(self, num_vertices, directed=False):
        super().__init__(num_vertices, directed)
        # self.matrix = np.zeros((num_vertices, num_vertices))
        self.matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, v1, v2, weight=1):
        if self.is_out_of_bound(v1) or self.is_out_of_bound(v2):
            raise ValueError(f"vertices {v1} and {v2} are out of bounds")

        if weight < 1:
            raise ValueError("An edge cannot have weight less than 1")

        self.matrix[v1][v2] = weight

        if not self.directed:
            self.matrix[v2][v1] = weight

    def get_adjacent_vertices(self, v):
        if self.is_out_of_bound(v):
            raise ValueError(f"cannot access vertex {v}")

        return [i for i in range(self.num_vertices) if self.matrix[v][i] > 0]

    def get_indegree(self, v):
        if self.is_out_of_bound(v):
            raise ValueError(f"cannot access vertex {v}")
        return len([i for i in range(self.num_vertices) if self.matrix[i][v] > 0])

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                print(i, ": ", v)


if __name__ == '__main__':
    g = AdjacencyMatrixGraph(4)
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