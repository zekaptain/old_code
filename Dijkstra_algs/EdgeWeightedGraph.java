
/**
 * EdgeWeightedGraph
 * 
 * Author: M. Q. Rieck
 * Date: September 2013
 * 
 */

// Class to represent an edge-weighted graph

public class EdgeWeightedGraph
{
   private int maxNumVertices;     // make room for how many vertices?
   private int maxNumEdges;        // make room for how many edges?
   private int maxVertexDegree;    // maximum degree of each vertex
   private int numVertices;        // how many actual vertices?
   private int numEdges;           // how many actual edges?
   private EWGVertex[] vertices;   // list of vertices in graph
   private EWGEdge[] edges;        // list of edges in graph
   
   public EdgeWeightedGraph(int maxNumVerts, int maxNumEdges, int maxVertDeg)
   {
      maxNumVertices = maxNumVerts;
      maxNumEdges = maxNumEdges;
      maxVertexDegree = maxVertDeg;
      numVertices = 0;
      numEdges = 0;
      vertices = new EWGVertex[maxNumVerts];
      edges = new EWGEdge[maxNumEdges];
   }
    
   public void addVertex(EWGVertex v) {
      vertices[numVertices++] = v;
   }
   public void addVertex(int id) { 
      vertices[numVertices++] =
         new EWGVertex(maxVertexDegree, id); 
   }
   public int getNumVertices() {
      return numVertices;
   }
   public EWGVertex getVertexAtIndex(int i) {
      return vertices[i];
   }
   public EWGVertex getVertexWithID(int id_) {
      for (int j=0; j<numVertices; j++)
        if (vertices[j].getID() == id_)   
          return vertices[j];
      return null;
   }
   public int getVertexIndex(EWGVertex v) {
      for (int j=0; j<numVertices; j++)
        if (vertices[j] == v)   
          return j;
      return -1;
   }
   public int getVertexIndex(int id_) {
      for (int j=0; j<numVertices; j++)
        if (vertices[j].getID() == id_)   
          return j;
      return -1;
   }
   public void addEdge(EWGVertex u, EWGVertex v, double weight)
   {
      EWGEdge e = edges[numEdges] = 
        new EWGEdge(u, v, weight);       
      u.addEdge(e);
      v.addEdge(e);
      numEdges++;
   }
   public void addEdge(int id1, int id2, double weight)
   {
      EWGVertex u = getVertexWithID(id1);
      EWGVertex v = getVertexWithID(id2);
      addEdge(u, v, weight);
   }
   public int getNumEdges() {
      return numEdges;
   }
   public EWGEdge getEdgeAtIndex(int i) {
      return edges[i];
   }
   public void reset() {
      for (int i=0; i<numVertices; i++) {
        vertices[i].setPrev(vertices[i]);
        vertices[i].unmark();
        vertices[i].setDistance(-1);
      }
      for (int i=0; i<numEdges; i++) 
        edges[i].deselect();
   }
   public void displayVertices() { 
      System.out.println("Number of vertices = " + numVertices);
      System.out.print("Vertices in graph:"); 
      for (int i=0; i<numVertices; i++) 
        System.out.print(" " + vertices[i].getID()); 
      System.out.println();
   }
   public void displayMarkedVertices() { 
      System.out.print("Marked vertices:"); 
      for (int i=0; i<numVertices; i++) 
        if (vertices[i].isMarked()) 
          System.out.print(" " + vertices[i].getID()); 
      System.out.println();
   }
   public void displayEdges() {
      System.out.println("Number of edges = " + numEdges);
      for (int i=0; i<numEdges; i++) edges[i].display(); 
   }
   public void display() {
      displayVertices(); 
      displayEdges();
   }
}
