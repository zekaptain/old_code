
/**
 * EWGVertex
 * 
 * Author: M. Q. Rieck
 * Date: September 2013
 * 
 */

// Class to represent vertices in an edge-weighted graph

public class EWGVertex
{
    private EWGEdge[] edges;     // edges incident with this vertex
    private int id, degree;
    private EWGVertex prev;      // Used in Kruskal's algorithm to
                                 // determine connected components
                                 // Also used in Dijkstra's algorithm
                                 // to detail reverse path
    private boolean marked;      // Used in Prim's and Dijkstra's algorithm
    private double distance;     // Used in Dijkstra's algorithm 
    
    // Pass an upper limit on vertex degree
    // Also pass an ID number for the new vertex 
    public EWGVertex(int maxDegree, int id_)
    {
        id = id_; 
        degree = 0; 
        edges = new EWGEdge[maxDegree]; 
        prev = this;
        marked = false;
        distance = -1;   // -1 stands for infinity here  
    }
    
    // Return integer ID of this vertex
    public int getID() { return id; }
    // How many edges come into this vertex?
    public int getDegree() { return degree; }
    public void addEdge(EWGEdge e) { 
        edges[degree++] = e;
    }
    public EWGEdge getEdgeAtIndex(int i) {
        return edges[i];
    }
    public void setPrev(EWGVertex v) { prev = v; } 
    public EWGVertex getPrev() { return prev; } 
    public EWGVertex getRep() {
        if (prev == this) return this;
        else return prev.getRep();
    }
    public void displayRep() {
       System.out.println("Vertex " + getID() +
          " is in component represented by vertex " + 
          getRep().getID());
    }    
    public boolean isMarked() { return marked; } 
    public void mark() { marked = true; }
    public void unmark() { marked = false; }
    public double getDistance() { return distance; }
    public void setDistance(double x) { distance = x; }    
}
