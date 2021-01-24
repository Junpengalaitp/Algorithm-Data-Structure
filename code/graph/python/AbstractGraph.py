import abc


class AbstractGraph(abc.ABC):
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight) -> None:
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass

    @abc.abstractmethod
    def get_indegree(self, v):
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2) -> int:
        pass

    @abc.abstractmethod
    def display(self) -> None:
        pass

    def is_out_of_bound(self, v) -> bool:
        return v < 0 or v >= self.num_vertices

