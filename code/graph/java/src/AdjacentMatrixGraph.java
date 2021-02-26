import java.util.Arrays;
import java.util.Collection;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class AdjacentMatrixGraph extends AbstractGraph<Integer> {

    private final int[][] matrix;

    public AdjacentMatrixGraph(int numOfVertices) {
        super(numOfVertices);
        this.matrix = new int[numOfVertices][numOfVertices];
    }

    public AdjacentMatrixGraph(int numOfVertices, boolean isDirected) {
        super(numOfVertices, isDirected);
        this.matrix = new int[numOfVertices][numOfVertices];
    }

    @Override
    public void addEdge(int v1, int v2, int weight) {
        if (isOutOfBound(v1) || isOutOfBound(v2)) {
            throw new IndexOutOfBoundsException();
        }
        if (weight < 1) {
            throw new IllegalArgumentException();
        }
        matrix[v1][v2] = weight;

        if (!isDirected) {
            matrix[v2][v1] = weight;
        }
    }

    @Override
    public void addEdge(int v1, int v2) {
        if (isOutOfBound(v1) || isOutOfBound(v2)) {
            throw new IndexOutOfBoundsException();
        }
        matrix[v1][v2] = 1;

        if (!isDirected) {
            matrix[v2][v1] = 1;
        }
    }

    @Override
    public Collection<Integer> getAdjacentVertices(int v) {
        return Arrays.stream(matrix[v])
                .filter(vx -> vx > 0)
                .boxed()
                .collect(Collectors.toList());
    }

    @Override
    public int getIndegree(int v) {
        return (int) Arrays.stream(matrix[v])
                .filter(vx -> vx > 0)
                .count();
    }

    @Override
    public int addEdgeWeight(int v1, int v2) {
        return matrix[v1][v2];
    }


    public static void main(String[] args) {
        AbstractGraph<Integer> graph = new AdjacentMatrixGraph(4);
        graph.addEdge(0, 1);
        graph.addEdge(0, 2);
        graph.addEdge(2, 3);

        IntStream.range(0, 4)
                .forEach(i -> System.out.println(i + " adjacent to: " + graph.getAdjacentVertices(i)));

        IntStream.range(0, 4)
                .forEach(i -> System.out.println(i + " indegree: " + graph.getIndegree(i)));

        IntStream.range(0, 4)
                .forEach(i -> {
                    graph.getAdjacentVertices(i)
                            .forEach(j -> System.out.println("edge weight: " + i + " " + j + " weight:" + graph.addEdgeWeight(i, j)));
                });

        graph.display();

    }
}


