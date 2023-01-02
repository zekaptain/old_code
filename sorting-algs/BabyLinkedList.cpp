#include <iostream>
#include <string>
using namespace std;  

struct Node {
  string guts; 
  Node* next; 
};

void addNewNodeToEnd(string s, Node*& first, Node*& last) {
  Node* p = new Node;
  p->guts = s; 
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

void addNewNodeToMiddle(string s, Node* ptr, Node*& first, Node*& last) {
  Node *p, *q; 
  if (ptr == NULL) { 
     // Assume linked list is empty, and so produce a linked list with 
	 // only one node. Change first and last accordingly. 
	 p = new Node; 
	 p->guts = s; 
	 p->next = NULL; 
	 first = last = p;
  } else { 
     // In this discussion, let "A" mean the node ptr is pointing to. 
	 // Let "B" mean the node that comes after "A". Let "C" mean the 
	 // newly created node. Begin by making q point to B. (If you're 
	 // confused, please please draw pictures!) 
     q = ptr->next; 
	 // Now create C and let p point to C. 
	 p = new Node; 
	 p->guts = s;
	 // Now rig it so C (not B) comes after A in the list 
	 ptr->next = p;
	 // Now rig it so B comes after C in the list 
	 p->next = q; 
	 // If q is NULL, then there really is no B, which means that the 
	 // new node C is actually the last node. So in this case ...
	 if (q == NULL) last = p;
  }
} 

// Display the contents of the linked list 
// when a pointer to the first node is passed. 
void displayList(Node* ptr) { 
   while (ptr != NULL) { 
      cout << ptr->guts << endl; 
	  ptr = ptr->next; 
   }   
   for (int i=0; i<20; i++) cout << '-'; 
   cout << endl; 
}

// Advance a pointer (ptr) some number of nodes (n) in the linked list 
void skipAhead(Node*& ptr, int n) {
   for (int i=0; i<n; i++) ptr = ptr->next; 
}

int main () {
    Node *first=NULL, *last=NULL, *ptr; 
	addNewNodeToEnd("duck", first, last); 
	addNewNodeToEnd("goose", first, last); 
	addNewNodeToEnd("swan", first, last); 
	addNewNodeToEnd("egret", first, last);
	addNewNodeToEnd("heron", first, last);
	addNewNodeToEnd("seagull", first, last); 
	displayList(first); 
	ptr = first; 
	skipAhead(ptr, 3); // change ptr to point to 4th node
	addNewNodeToMiddle("pelican", ptr, first, last); 
	displayList(first); 
	addNewNodeToMiddle("albatross", last, first, last); 
	displayList(first); 
	
	
    return 0;
}
