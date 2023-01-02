
/**
 * EWGEdge
 * 
 * Author: M. Q. Rieck
 * Date: September 2013
 * 
 */

// Class to represent edges in an edge-weighted graph

public class EWGEdge
{
    private EWGVertex first, second;  // connected vertices 
    private double weight;            // edge weight 
    private boolean selected; // used in Kruskal's and Prim's algorithms
    
    public EWGEdge(EWGVertex u, EWGVertex v, double w) 
    {
       first = u;
       second = v;
       weight = w; 
       selected = false;
    }
   
    public EWGVertex getFirstVertex() { return first; } 
    public EWGVertex getSecondVertex() { return second; } 
    public double getWeight() { return weight; } 
    public EWGVertex getOtherVertex(EWGVertex v) {
       if (v == first) return second;
       if (v == second) return first;
       return null;
    }
    public boolean isSelected() { return selected; }
    public void select() { selected = true; }
    public void deselect() { selected = false; }
    public void display() {
       System.out.println("edge connecting vertex " + 
         first.getID() + " and vertex " + second.getID() +
         " of weight " + weight);
    }            
    // Call this in Kruskal to test this edge, to avoid cycles
    public boolean sameComponent() {
       return first.getRep() == second.getRep();
    }
    // Call this in Kruskal after selecting this edge
    public void changeComponents() {
       first.getRep().setPrev(second.getRep());       
    }
}
