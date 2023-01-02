
/**
 * Dijkstra
 * 
 * Author: M. Q. Rieck
 * Date: September 2013
 * 
 */

// Code to demonstrate Dijkstra's algorithm

public class Dijkstra
{
   public static EdgeWeightedGraph buildEdgeWeightedGraph() {
      // Sample data for edge-weighted graph: 
      int numVertices = 7;
      int vertexIDs[] = {11, 22, 33, 44, 55, 66, 77}; 
      int numEdges = 10;
      // IDs of first vertices in edges
      int firstVertexIDs[] = 
        {11, 11, 11, 22, 22, 33, 33, 44, 55, 66};
      // IDs of second vertices in edges
      int secondVertexIDs[] =
        {22, 33, 55, 44, 55, 44, 66, 55, 66, 77};
      // Edge weights
      double edgeWeights[] = 
        {1.3, 3.2, 9.3, 2.2, 1.1, 9.1, 1.9, 5.8, 7.2, 5.9};

      EdgeWeightedGraph graph = 
        new EdgeWeightedGraph(numVertices, numEdges, numVertices);
      for (int i=0; i<numVertices; i++)
        graph.addVertex(vertexIDs[i]); 
      for (int i=0; i<numEdges; i++) 
        graph.addEdge(firstVertexIDs[i], secondVertexIDs[i], edgeWeights[i]); 
      return graph;
   }

   public static void DijkstraAlgorithm(EdgeWeightedGraph graph, 
    EWGVertex startVertex, EWGVertex endVertex) {
      EWGVertex visitVertex = startVertex;
      ReverseHeap<EWGVertex> queue = new ReverseHeap<EWGVertex>();
      graph.reset();
      startVertex.setDistance(0); 
      // Put starting vertex into to-be-visited queue
      queue.insertNode(startVertex, 0);
      // Repeatedly visit and process the vertex in the
      // queue that is closest to the starting vertex
      while (queue.getSize() > 0) {
         visitVertex = queue.removeTopOfHeap();
         visitVertex.mark();
         if (visitVertex == endVertex) break;
         for (int i=0; i<visitVertex.getDegree(); i++) {
           EWGEdge e = visitVertex.getEdgeAtIndex(i);
           EWGVertex u = e.getOtherVertex(visitVertex);
           if (!u.isMarked()) {
             if (
               u.getDistance() < 0  // really infinity
             ) {
               // First time u is discovered, so set its distance 
               // from starting vertex  
               u.setDistance(
                 visitVertex.getDistance() + e.getWeight()
               );
               // Remember the path back to starting vertex
               u.setPrev(visitVertex);
               // Put u in the to-be-visited queue too
               queue.insertNode(u, u.getDistance());
             } else if (u.getDistance() > 
               visitVertex.getDistance() + e.getWeight()
             ) { 
               // Not first time u is discovered, but a shorter path 
               // found, so change its distance from starting vertex
               u.setDistance(
                 visitVertex.getDistance() + e.getWeight()
               );
               // Change the path back to starting vertex too
               u.setPrev(visitVertex);
               // And change u's priority in the to-be-visited queue
               queue.changePriority(u, u.getDistance());
             }
           }            
         }
      }
      if (visitVertex == endVertex) {
        System.out.print("Reverse path:");
        EWGVertex v = endVertex;
        System.out.print(" " + v.getID());
        while (v != startVertex) { 
           v = v.getPrev(); 
           System.out.print(" " + v.getID());
        }
        System.out.println();
      }
   }

   public static void main(String[] args) {
      EdgeWeightedGraph graph = buildEdgeWeightedGraph();
      graph.display();
      EWGVertex startVertex = graph.getVertexAtIndex(0);
      EWGVertex endVertex = graph.getVertexAtIndex(
        graph.getNumVertices()-1);
      System.out.println(
        "Using Dijkstra's algorithm to find shortest path from vertex " +
        startVertex.getID() + " to vertex " + endVertex.getID() + "."); 
      DijkstraAlgorithm(graph, startVertex, endVertex);
   }
}


