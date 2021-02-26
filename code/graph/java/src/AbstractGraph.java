import java.util.Collection;
import java.util.stream.IntStream;

public abstract class AbstractGraph<T> {

    protected int numOfVertices;
    protected boolean isDirected;

    public AbstractGraph(int numOfVertices) {
        this.numOfVertices = numOfVertices;
        this.isDirected = false;
    }

    public AbstractGraph(int numOfVertices, boolean isDirected) {
        this.numOfVertices = numOfVertices;
        this.isDirected = isDirected;
    }

    public abstract void addEdge(int v1, int v2, int weight);

    public abstract void addEdge(int v1, int v2);

    public abstract Collection<T> getAdjacentVertices(int v);

    public abstract int getIndegree(int v);

    public abstract int addEdgeWeight(int v1, int v2);

    protected void display() {
        IntStream.range(0, numOfVertices)
                .forEach(i -> getAdjacentVertices(i)
                        .forEach(v -> System.out.println(i + " : " + v)));
    }

    protected boolean isOutOfBound(int v) {
        return v < 0 || v >= numOfVertices;
    }
}
