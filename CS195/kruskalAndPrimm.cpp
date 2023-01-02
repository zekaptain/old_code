// KruskalAndPrim.cpp

// Code to demonstrate Kruskal's and Prim's algorithms

// Author: M. Q. Rieck
// Date: September 2013

#include <iostream>
#include <string>

using namespace std;

void testKruskalAndPrim();

int main() {

    testKruskalAndPrim();
    return 0;

}


class EWGVertex;
class EWGEdge;

// Class to represent vertices in an edge-weighted graph

class EWGVertex
{
  private:
  
    EWGEdge **edges;             // edges incident with this vertex
    int id, degree;
    EWGVertex *prev;             // Used in Kruskal's algorithm to
                                 // determine connected components
                                 // Also used in Dijkstra's algorithm
                                 // to detail reverse path
    bool marked;                 // Used in Prim's and Dijkstra's algorithm
    double distance;             // Used in Dijkstra's algorithm 
  
  public:
  
    // Pass an upper limit on vertex degree
    // Also pass an ID number for the new vertex 
    EWGVertex(int maxDegree, int id_)
    {
        id = id_; 
        degree = 0; 
        edges = new EWGEdge*[maxDegree]; 
        prev = this;
        marked = false;
        distance = -1;   // -1 stands for infinity
    }
    
    // Return integer ID of this vertex
    int getID() { return id; }
    // How many edges come into this vertex?
    int getDegree() { return degree; }
    void addEdge(EWGEdge *e) { 
        edges[degree++] = e;
    }
    EWGEdge* getEdgeAtIndex(int i) {
        return edges[i];
    }
    void setPrev(EWGVertex *v) { prev = v; } 
    EWGVertex* getPrev() { return prev; } 
    EWGVertex* getRep() {
        if (prev == this) return this;
        else return prev->getRep();
    }
    void displayRep() {
       cout << "Vertex " << getID() <<
          " is in component represented by vertex " << 
          getRep()->getID();
    }    
    bool isMarked() { return marked; } 
    void mark() { marked = true; }
    void unmark() { marked = false; }
    double getDistance() { return distance; }
    void setDistance(double x) { distance = x; }    
};


// Class to represent edges in an edge-weighted graph

class EWGEdge
{
  private:
  
	EWGVertex *first, *second;  // connected vertices 
    double weight;              // edge weight 
    bool selected;           // used in Kruskal's and Prim's algorithms
    
  public:
  
    EWGEdge(EWGVertex *u, EWGVertex *v, double w) 
    {
       first = u;
       second = v;
       weight = w; 
       selected = false;
    }
   
    EWGVertex* getFirstVertex() { return first; } 
    EWGVertex* getSecondVertex() { return second; } 
    double getWeight() { return weight; } 
    EWGVertex* getOtherVertex(EWGVertex *v) {
       if (v == first) return second;
       if (v == second) return first;
       return NULL;
    }
    bool isSelected() { return selected; }
    void select() { selected = true; }
    void deselect() { selected = false; }
    void display() {
       cout << "edge connecting vertex " <<
         first->getID() << " and vertex " << second->getID()
         << " of weight " << weight << endl;
    }            
    // Call this in Kruskal to test this edge, to avoid cycles
    bool sameComponent() {
       return first->getRep() == second->getRep();
    }
    // Call this in Kruskal after selecting this edge
    void changeComponents() {
       first->getRep()->setPrev(second->getRep());       
    }
};


// Class to represent an edge-weighted graph

class EdgeWeightedGraph
{
  private:
   
   int maxNumVertices;     // make room for how many vertices?
   int maxNumEdges;        // make room for how many edges?
   int maxVertexDegree;    // maximum degree of each vertex
   int numVertices;        // how many actual vertices?
   int numEdges;           // how many actual edges?
   EWGVertex **vertices;   // list of vertices in graph
   EWGEdge **edges;        // list of edges in graph
   
  public:
  
   EdgeWeightedGraph(int maxNumVerts, int maxNumEdges, int maxVertDeg)
   {
      maxNumVertices = maxNumVerts;
      maxNumEdges = maxNumEdges;
      maxVertexDegree = maxVertDeg;
      numVertices = 0;
      numEdges = 0;
      vertices = new EWGVertex*[maxNumVerts];
      edges = new EWGEdge*[maxNumEdges];
   }
    
   void addVertex(EWGVertex *v) {
      vertices[numVertices++] = v;
   }
   void addVertex(int id) { 
      vertices[numVertices++] =
         new EWGVertex(maxVertexDegree, id); 
   }
   int getNumVertices() {
      return numVertices;
   }
   EWGVertex* getVertexAtIndex(int i) {
      return vertices[i];
   }
   EWGVertex* getVertexWithID(int id_) {
      for (int j=0; j<numVertices; j++)
        if (vertices[j]->getID() == id_)   
          return vertices[j];
      return NULL;
   }
   int getVertexIndex(EWGVertex *v) {
      for (int j=0; j<numVertices; j++)
        if (vertices[j] == v)   
          return j;
      return -1;
   }
   int getVertexIndex(int id_) {
      for (int j=0; j<numVertices; j++)
        if (vertices[j]->getID() == id_)   
          return j;
      return -1;
   }
   void addEdge(EWGVertex *u, EWGVertex *v, double weight)
   {
      EWGEdge* e = edges[numEdges] = 
        new EWGEdge(u, v, weight);       
      u->addEdge(e);
      v->addEdge(e);
      numEdges++;
   }
   void addEdge(int id1, int id2, double weight)
   {
      EWGVertex* u = getVertexWithID(id1);
      EWGVertex* v = getVertexWithID(id2);
      addEdge(u, v, weight);
   }
   int getNumEdges() {
      return numEdges;
   }
   EWGEdge* getEdgeAtIndex(int i) {
      return edges[i];
   }
   void reset() {
      for (int i=0; i<numVertices; i++) {
        vertices[i]->setPrev(vertices[i]);
        vertices[i]->unmark();
        vertices[i]->setDistance(-1);
      }
      for (int i=0; i<numEdges; i++) 
        edges[i]->deselect();
   }
   void displayVertices() { 
      cout << "Number of vertices = " << numVertices << endl;
      cout << "Vertices in graph:"; 
      for (int i=0; i<numVertices; i++) 
        cout << " " << vertices[i]->getID(); 
      cout << endl;
   }
   void displayMarkedVertices() { 
      cout << "Marked vertices:"; 
      for (int i=0; i<numVertices; i++) 
        if (vertices[i]->isMarked()) 
          cout << " " << vertices[i]->getID(); 
      cout << endl;
   }
   void displayEdges() {
      cout << "Number of edges = " << numEdges << endl;
      for (int i=0; i<numEdges; i++) edges[i]->display(); 
      cout << endl;
   }
   void display() {
      displayVertices(); 
      displayEdges();
   }
};


EdgeWeightedGraph* buildEdgeWeightedGraph() 
{
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

   EdgeWeightedGraph* graph = 
     new EdgeWeightedGraph(numVertices, numEdges, numVertices);
   for (int i=0; i<numVertices; i++)
     graph->addVertex(vertexIDs[i]); 
   for (int i=0; i<numEdges; i++) 
     graph->addEdge(firstVertexIDs[i], secondVertexIDs[i], edgeWeights[i]); 
   return graph;
}

void KruskalAlgorithm(EdgeWeightedGraph *graph) 
{
   int selectIndex = 0, numSelected = 0, i;
   bool noEdgeYet = true;
   double minWeight = 0, totalWeight = 0;
   int* selected = new int[graph->getNumEdges()];
   graph->reset();
   EWGEdge* e = graph->getEdgeAtIndex(0);
   // Repeatedly select the lowest weight edge that does
   // not introduce a cycle among the selected edges 
   while (selectIndex >= 0) {
     selectIndex = -1;
     noEdgeYet = true;
     for (i=0; i<graph->getNumEdges(); i++) {
	     e = graph->getEdgeAtIndex(i); 
	   if (!e->isSelected() && !e->sameComponent() && (noEdgeYet || e->getWeight() < minWeight)) {
        selectIndex = i;
		    minWeight = e->getWeight();
		    noEdgeYet = false;            
	   }
	 }
	 if (selectIndex >= 0) {
	   e = graph->getEdgeAtIndex(selectIndex); 
       e->select(); 
       // After selecting the edge, make a change to reflect
       // which vertices are now connected via selected edges
       e->changeComponents();  
       selected[numSelected++] = selectIndex;
       totalWeight += minWeight;
     }
   }
   cout << "Kruskal selected these edges (in order):" << endl;
   for (i=0; i<numSelected; i++) 
     graph->getEdgeAtIndex(selected[i])->display();
   cout << "Total weight = " << totalWeight << endl << endl;
}

void PrimAlgorithm(EdgeWeightedGraph *graph) 
{
   int vertexIndex = 0, edgeIndex = 0, numSelected = 0, i, j;
   bool noEdgeYet = true;
   double minWeight = 0, totalWeight = 0;
   int* selected = new int[graph->getNumEdges()];
   EWGVertex *v;
   EWGEdge *e;
   graph->reset();
   while (vertexIndex >= 0) {
     vertexIndex = -1;
     for (i=0; i<graph->getNumVertices(); i++)
	 if (!graph->getVertexAtIndex(i)->isMarked()) break;
	 // If some vertex is not yet connected with a selected edge,
	 // then use it as a start for a new tree of selected edges
	 if (i<graph->getNumVertices()) {
	   vertexIndex = i;
	   graph->getVertexAtIndex(i)->mark();
	   edgeIndex = 0;
	   // Keep building the tree as long as possible by selecting
	   // a minimal weight edge connecting the tree to another vertex
	   while (edgeIndex >= 0) {
	      noEdgeYet = true;
		    edgeIndex = -1;
		    for (j=0; j<graph->getNumEdges(); j++) {
		      e = graph->getEdgeAtIndex(j);
		      if (((e->getFirstVertex()->isMarked() && !e->getSecondVertex()->isMarked()) ||(!e->getFirstVertex()->isMarked() && e->getSecondVertex()->isMarked())) &&(noEdgeYet || e->getWeight() < minWeight)) {
		        edgeIndex = j;
			      minWeight = e->getWeight();
			      noEdgeYet = false;
		      }               
		    }
		    if (edgeIndex >= 0) {
		      e = graph->getEdgeAtIndex(edgeIndex);
		      e->select();
		      // After selecting an edge, remember its vertices too
		      e->getFirstVertex()->mark();
		      e->getSecondVertex()->mark();
		      selected[numSelected++] = edgeIndex;                
		      totalWeight += minWeight;
		    }
	    }   
	  } 
	}
	cout << "Prim selected these edges (in order):" << endl; 
	for (i=0; i<numSelected; i++)
	  graph->getEdgeAtIndex(selected[i])->display();
	cout << "Total weight = " << totalWeight << endl << endl;
}

void testKruskalAndPrim() {
   EdgeWeightedGraph* graph = buildEdgeWeightedGraph();
   graph->display();
   KruskalAlgorithm(graph);
   PrimAlgorithm(graph);
}
