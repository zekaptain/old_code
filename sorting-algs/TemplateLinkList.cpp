
// A template version of my basic linked list code

#include <iostream>
#include <string>
using namespace std;  

template<typename T>
struct Node {
  T guts; 
  Node<T>* next; 
};

// Create a node and add it to the end of linked list 
template<typename T>
void addNewNodeToEnd(T data, Node<T>*& first, 
 Node<T>*& last) {
  Node<T>* p = new Node<T>;
  p->guts = data; 
  p->next = NULL; 
  if (last == NULL) { 
	first = last = p; 
  } else { 
    last->next = p; 
	last = p;
  } 
}

// Create a node and add it to the middle of linked list 
// (ptr points to existing node that will come before new node) 
template<typename T>
void addNewNodeToMiddle(T data, Node<T>* ptr, Node<T>*& first, Node<T>*& last) {
  Node<T> *p, *q; 
  if (ptr == NULL) { 
	 p = new Node<T>; 
	 p->guts = data; 
	 p->next = NULL; 
	 first = last = p;
  } else { 
     q = ptr->next; 
	 p = new Node<T>; 
	 p->guts = data;
	 ptr->next = p;
	 p->next = q; 
	 if (q == NULL) last = p;
  }
} 

// Advance a pointer (ptr) some number of nodes 
// (n) in the linked list 
template <typename T>
void skipAhead(Node<T>*& ptr, int n) {
   for (int i=0; i<n; i++) ptr = ptr->next; 
}

// Display the contents of the linked list
// when a pointer to the first node is passed. 
template <typename T>
void displayList(Node<T>* ptr) {
   while (ptr != NULL) { 
      cout << ptr->guts << endl;
	  ptr = ptr->next; 
   }   
   for (int i=0; i<20; i++) cout << '-'; 
   cout << endl; 
}

// Now test
int main () {
    Node<string> *first=NULL, *last=NULL, *ptr; 
	addNewNodeToEnd<string>("duck", first, last); 
	addNewNodeToEnd<string>("goose", first, last); 
	addNewNodeToEnd<string>("swan", first, last); 
	addNewNodeToEnd<string>("egret", first, last);
	addNewNodeToEnd<string>("heron", first, last);
	addNewNodeToEnd<string>("seagull", first, last); 
	displayList<string>(first); 
	ptr = first; 
	skipAhead<string>(ptr, 3); // change ptr to point to 4th node
	addNewNodeToMiddle<string>("pelican", ptr, first, last); 
	displayList<string>(first); 
	addNewNodeToMiddle<string>("albatross", last, first, last); 
	displayList<string>(first); 		
    return 0;
}
