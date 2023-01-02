

// HeapAndHeapsort.cpp

// Code to demonstrate heaps and Heapsort

// Author: M. Q. Rieck
// Date: June 2013

#include <iostream>
#include <string>

using namespace std;

//declares a function
void testHeapAndHeapsort();



// EXECUTION STARTS HERE

int main() {
    
    testHeapAndHeapsort();
    return 0;
    
}



// A class of objects to put into the heap
class Vehicle
{
private:
    string name;
    double weight;		 // not used in this example
public:
    //accessor methods -- one returns name, other weight
    Vehicle() {
        name = "";
        weight = -1;
    }
    Vehicle(string n, double w) {
        name = n;
        weight = w;
    }
    string getName() { return name; }
    double getWeight() { return weight; }
};

// Make sure a vehicle can be displayed
ostream& operator<<(ostream& os, Vehicle& v) {
    return os << v.getName();
}



// An object from this class is a heap containing generic
// data, along with a priority number for each item. Once
// a heap has been built, it can also be used to Heapsort.

//keyword template figures out details of class.
//allows you to make lots of similar classes that are related
//this function describes the characteristics of those classes
template<typename Data>
class HeapAndHeapsort {
    
private:
    
    static const int MAX_SIZE = 100;
    // An array of objects to maintain in heap
    Data data[MAX_SIZE];
    // An array of associated priorities
    int priorities[MAX_SIZE];
    // Size of heap (# nodes in it)
    int heapsize;
    
    inline void swapInHeap(int i, int j)
    {
        Data temp = data[i];
        int priority = priorities[i];
        data[i] = data[j];
        priorities[i] = priorities[j];
        data[j] = temp;
        priorities[j] = priority;
    }
    //inline is request to compiler
    //if it's at all possible, try to speed things up
    //by not making usual function calls
    //but by copying code in function there to avoid time
    //it takes to do function call
    inline int parent(int n) { return n/2; }
    inline int leftChild(int n) { return 2*n; }
    inline int rightChild(int n) { return 2*n+1; }
    
public:
    
    HeapAndHeapsort() {
        heapsize = 0;
    }
    
    // Return number of nodes in the heap
    int getSize() { return heapsize; }
    
    // Add a data with priority to heap, and heapify up
    //pass in vehicle object (d) and its priority
    void insertNode(Data d, int priority) {
        int index = ++heapsize;
        data[index] = d;
        priorities[index] = priority;
        //only swap if priority is greater than 1
        //and child node is greater than parent node
        while (index > 1 && priorities[index] > priorities[parent(index)])
        {
            swapInHeap(index, parent(index));
            //critically important to move index b/c
            //when you swap vehicle in this,
            //need to change index to where you swapped it to
            //if index was 6, change it to its parent (6) if #
            //was actually swapped w/ its parent
            index = parent(index);
        }
    }
    
    // Remove and return data on top of heap, and HEAPIFY DOWN
    Data removeTopOfHeap() {
        //indexM holds position of the biggest priority of parent, left child, and right child
        int index = 1, indexL, indexR, indexM;
        // Swap first and last in array
        swapInHeap(1, heapsize);
        //decrements heapsize. last thing in array is still in array,
        //but it's no longer a part of the heap since heapsize has been decremented by 1
        heapsize--;
        // Heapify down starting at top
        while(index < heapsize) {
            // do child nodes have higher priority?
            indexM = indexL = indexR = index;
            //if index has a left child and it's <= heapsize, there is a left child in heap
            if (leftChild(index) <= heapsize) {
                indexL = leftChild(index);
                if (priorities[indexM] < priorities[indexL])
                    //left child has biggest priority
                    indexM = indexL;
            }
            //if index has right child and <= heapsize, there is a right child in heap
            if (rightChild(index) <= heapsize) {
                indexR = rightChild(index);
                if (priorities[indexM] < priorities[indexR])
                    //right child has biggest priority
                    indexM = indexR;
            }
            // swap with a child or quit heapifying?
            //if a child node has biggest priority, swap
            //indexM will equal index of parent has highest priority
            if (indexM != index) {
                swapInHeap(index, indexM);
                index = indexM;
            } else {
                break;
            }
        }
        return data[heapsize+1];
    }
    
    // Display heap
    void display() {
        for (int i=1; i <= heapsize; i++)
            cout << "(" << data[i] << ":" << priorities[i] << ") ";
        cout << endl;
        cout << endl;
    }
    
    // Display each level of heap on separate line
    void displayLevels() {
        int count = 0, mark = 1;
        cout << "Levels of the heap:" << endl;
        for (int i=1; i <= heapsize; i++) {
            cout << "(" << data[i] << ":" << priorities[i] << ") ";
            if (++count == mark) {
                cout << endl;
                count = 0;
                mark *= 2;
            }
        }
        cout << endl;
        cout << endl;
    }
    
    // Heapsort amounts to repeatedly removing fro  m the top of the heap
    // and putting this in the array right after the active portion
    void heapsort() {
        int holdsize = heapsize;
        while (heapsize > 0) removeTopOfHeap();
        heapsize = holdsize;
    }
};



// Test code for heap and Heapsort
void testHeapAndHeapsort()
{
    //implements keyword template w/ characteristics of HeapAndHeapsort class
    HeapAndHeapsort<Vehicle> heap;
    heap.insertNode(Vehicle("Car", 1724.4), 31);
    heap.displayLevels();
    heap.insertNode(Vehicle("Boat", 2523.6), 15);
    heap.displayLevels();
    heap.insertNode(Vehicle("Plane", 7482.9), 47);
    heap.displayLevels();
    heap.insertNode(Vehicle("Rocket", 1527274.5), 55);
    heap.displayLevels();
    heap.insertNode(Vehicle("Bicycle", 19.3), 23);
    heap.displayLevels();
    heap.insertNode(Vehicle("Motorcycle", 441.9), 42);
    heap.displayLevels();
    heap.insertNode(Vehicle("Starship", 1735399121.8), 44);
    heap.displayLevels();
    heap.insertNode(Vehicle("Bathysphere", 2121.8), 51);
    heap.displayLevels();
    cout << "The heap as a list: ";
    heap.display();
    heap.heapsort();
    cout << "After Heapsorting: ";
    heap.display();
}