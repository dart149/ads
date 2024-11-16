import java.util.PriorityQueue;
import java.util.*;

class Pair{
    int node;
    int weight;
    Pair(int node,int weight){
        this.node=node;
        this.weight=weight;
    }
}
public class prims {
    public static int spanningTree(int[][] adjmat,int n){
        PriorityQueue<Pair> pq = new PriorityQueue<>((x,y)->x.weight-y.weight);
        pq.add(new Pair(0, 0));
        int[] parent = new int[n];
        Arrays.fill(parent,-1);
        int[] vis = new int[n];
        int sum=0;
        while(!pq.isEmpty()){
         int node = pq.peek().node;
         int weight = pq.peek().weight;
         pq.remove();
         if(vis[node]==1) continue;
         vis[node]=1;
         sum+=weight;
         if(parent[node]!=-1){
             System.out.println(parent[node]+" - "+node);
         }
         for(int i=0;i<n;i++){
             int edgwt = adjmat[node][i];
             if(edgwt!=0 && vis[i]==0){
                 pq.add(new Pair(i, edgwt));
                 parent[i]=node;
             }
         }
       
    }
    return sum;
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
        
        int totalWeight = spanningTree(adjMatrix,V);
        System.out.println("Sum of weights of edges in the Minimum Spanning Tree: " + totalWeight);
    }
}
