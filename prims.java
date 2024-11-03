import java.util.*;

class Pair {
    int node;
    int distance;

    public Pair(int distance, int node) {
        this.node = node;
        this.distance = distance;
    }
}

public class Main {
    // Function to find sum of weights of edges of the Minimum Spanning Tree using Prim's Algorithm
    static int spanningTree(int V, int[][] adjMatrix) {
        // Priority queue to pick the edge with the minimum weight
        PriorityQueue<Pair> pq = new PriorityQueue<>((x, y) -> x.distance - y.distance);

        // Visited array to keep track of nodes already included in MST
        int[] vis = new int[V];

        // Parent array to store the parent of each node in MST
        int[] parent = new int[V];
        Arrays.fill(parent, -1);

        // Add the starting node (node 0) with weight 0
        pq.add(new Pair(0, 0));

        int sum = 0; // Variable to store sum of weights in MST

        while (!pq.isEmpty()) {
            int wt = pq.peek().distance;
            int node = pq.peek().node;
            pq.remove();

            // If the node is already visited, continue to next
            if (vis[node] == 1) continue;

            // Include the node in MST
            vis[node] = 1;
            sum += wt;

            // Print the edge if the node has a valid parent
            if (parent[node] != -1) {
                System.out.println("Edge: " + parent[node] + " - " + node + " with weight: " + wt);
            }

            // Check all adjacent nodes of the current node
            for (int adjNode = 0; adjNode < V; adjNode++) {
                int edgeWeight = adjMatrix[node][adjNode];

                // If there's an edge and the adjacent node is not visited, add to priority queue
                if (edgeWeight != 0 && vis[adjNode] == 0) {
                    pq.add(new Pair(edgeWeight, adjNode));
                    parent[adjNode] = node; // Set the parent of adjNode as the current node
                }
            }
        }

        return sum; // Return the sum of weights in MST
    }

    public static void main(String[] args) {
        int V = 5; // Number of vertices
        int[][] adjMatrix = {
            {0, 2, 0, 6, 0},
            {2, 0, 3, 8, 5},
            {0, 3, 0, 0, 7},
            {6, 8, 0, 0, 9},
            {0, 5, 7, 9, 0}
        };
        
        int totalWeight = spanningTree(V, adjMatrix);
        System.out.println("Sum of weights of edges in the Minimum Spanning Tree: " + totalWeight);
    }
}
