import java.util.*;

public class DFS {

    private int vertices;
    private LinkedList<Integer>[] adjList;

    DFS(int v) {
        vertices = v;
        adjList = new LinkedList[v];
        for (int i = 0; i < v; i++)
            adjList[i] = new LinkedList<>();
    }

    void addEdge(int v, int w) {
        adjList[v].add(w);
    }

    void dfsUtil(int node, boolean[] visited) {
        visited[node] = true;
        System.out.print(node + " ");

        for (int neighbour : adjList[node]) {
            if (!visited[neighbour]) {
                dfsUtil(neighbour, visited);
            }
        }
    }

    void dfs(int start) {
        boolean[] visited = new boolean[vertices];
        dfsUtil(start, visited);
    }

    public static void main(String[] args) {
        DFS g = new DFS(5);

        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 3);
        g.addEdge(2, 4);

        System.out.println("DFS Traversal:");
        g.dfs(0);
    }
}