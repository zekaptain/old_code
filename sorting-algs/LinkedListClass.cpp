#include <iostream>
#include <string>
using namespace std;  

struct Node {
  string data; 
  Node* next; 
};

class LinkedList {
  private: 
    Node* first;
	Node* last; 
  public: 
    // Default constructor is easy here 
    LinkedList() { 
	  first = last = NULL; 
	}
	// Destructor - getting rid of a LinkedList object should 
	// also eliminate all of its Node structures
	~LinkedList() {
	  Node* ptr = first; 
	  Node* nextPtr; 
	  while (ptr != NULL) { 
		nextPtr = ptr->next; 
		delete ptr;  // delete the Node that ptr points to 
		ptr = nextPtr; 
	  } 
	}
	// Method for adding a new node, with a given string, to
	// the end of the linked list 
	void addNewNodeToEnd(string s) {
      Node* p = new Node;
      p->data = s; 
      p->next = NULL; 
      if (last == NULL) { 
        // if list is currently empty, then just rig it so that the
	    // new node is both the first and the last node in the list 
        first = last = p; 
      } else { 
        // last still points to the "old last" node. This should 
	    // become then next-to-last node, so set its next pointer
	    // to point to the "new last" node. 
        last->next = p; 
	    // Change the last variable to reflect the fact that there is 
	    // now a new last node.
	    last = p;
      } 
    }
    // Display the contents of the linked list 
    // when a pointer to the first node is passed. 
    void displayList() { 
	  Node* ptr = first; 
      while (ptr != NULL) { 
		cout << ptr->data << endl; 
	    ptr = ptr->next; 
      }   
      for (int i=0; i<20; i++) cout << '-'; 
      cout << endl; 
    }
}; 

// Now test
int main () {
	LinkedList aquaticBirds; 
	aquaticBirds.addNewNodeToEnd("duck"); 
	aquaticBirds.addNewNodeToEnd("goose"); 
	aquaticBirds.addNewNodeToEnd("swan"); 
	aquaticBirds.addNewNodeToEnd("egret");
	aquaticBirds.addNewNodeToEnd("heron");
	aquaticBirds.addNewNodeToEnd("seagull"); 
	aquaticBirds.displayList(); 
    return 0;
}

