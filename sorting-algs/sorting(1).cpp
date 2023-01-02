
// Sorting.cpp

// Demo of Various Sorting Algorithms

// Author: M. Q. Rieck
// Date: June, 2013

#include <iostream>
#include <ctime>

// Define DISPLAY only if you want to see the original random array and the sorted.
// Otherwise, comment out the next definition:

// #define DISPLAY

// SIZE is the size (length) of the random array

//#define SIZE 100
#define SIZE 60000

using namespace std;

double a[SIZE], b[SIZE];

void compareSortingMethods();


// EXECUTION STARTS HERE 
int main() 
{
	compareSortingMethods();
}

// Fill up an array randomly
void random_fill(double p[]) {
	for (int i = 0; i < SIZE; i++)
		p[i] = (rand() % 1000000) / 10000.0;
}

// Copy one array to another
void copy(double p[], double q[]) {
	for (int i = 0; i < SIZE; i++) q[i] = p[i];
}

// Display an array
void display(double p[]) {
#ifdef DISPLAY
	for (int i = 0; i < SIZE; i++) cout << p[i] << " ";
	cout << endl;
#endif
}

void bubbleSort(double array[]) 
{
	// make SIZE-1 passes through array
	for (int i = SIZE; i > 1; i--)		
		// scan from start to some point
		for (int j = 1; j < i; j++)
			// swap pair of entries?
			if (array[j-1] > array[j]) {
			  double temp = array[j-1];
			  array[j-1] = array[j];
			  array[j] = temp;
			}
}

void selectionSort(double array[]) 
{
	int i, j, min, SIZE1 = SIZE-1;
	// make SIZE-1 passes through array
	for (i = 0; i < SIZE1; i++) {
		// scan from some point to end
		for (min = i, j = i+1; j < SIZE; j++)
		// remember position of minimum value 
		if (array[j] < array[min]) min = j;
		// swap to move minimum into correct spot
		double temp = array[i];
		array[i] = array[min]; 
		array[min] = temp; 
	}
}

void insertionSort(double array[]) 
{
	int i, j;
	// process entries from 2nd spot to end
	for (i = 1; i < SIZE; i++) {
		double tmp = array[i];
		// shift some initial entries to the right
		for (j = i; j > 0 && tmp < array[j-1]; j--)
			array[j] = array[j-1];
		// put entry being processed into the correct spot
		array[j] = tmp;
	}
}

void mergesort(double a1[], double a2[], int left=0, int right=SIZE-1) 
{
	int i, j, k, middle; 
	if (left < right) {
		middle = (left + right) / 2; 
		// Sort left half (using recursive call)
		mergesort(a1, a2, left, middle);
		// Sort right half (using recursive call)
		mergesort(a1, a2, middle+1, right);
		// Now merge the halves into auxiliary array
		k = i = left; j = middle+1;
		while (i <= middle && j <= right)
		  a2[k++] = ( a1[i] <= a1[j] 
			? a1[i++] : a1[j++] );
		// Get what still remains in left half
		while (i <= middle) a2[k++] = a1[i++];
		// Get what still remains in right half
		while (j <= right) a2[k++] = a1[j++];
		// Copy back from auxiliary array to main array
		for (i = left; i <= right; i++) a1[i] = a2[i];
	}
}  

void mergesort(double array[]) 
{
        double auxArray[SIZE]; 
        mergesort(array, auxArray, 0, SIZE-1);
}
    
void quicksort(double array[], int left=0, int right=SIZE-1) 
{
	double pivot, temp; 
	int i, j; 
	if (left < right) { 
		// pivot is entry furthest right
		// until just before recursive calls
		pivot = array[right];
		// keep stuff <= pivot in slots from left to i
		i = left - 1; 
		for (j = left; j <= right; j++)
		  if (array[j] <= pivot) {
			temp = array[++i];
			array[i] = array[j];
			array[j] = temp;
		}
		// Now sort stuff before pivot 
		quicksort(array, left, i-1);
		// Now sort stuff after pivot 
		quicksort(array, i+1, right);
	}
}       

void compareSortingMethods() 
{
	clock_t start_time, end_time;
	srand(time(0));
	random_fill(a);
#ifdef DISPLAY
    cout << "Original random array:" << endl; 
#endif
    display(a);
    copy(a, b);
    start_time = clock();
    bubbleSort(b);
    end_time = clock();
    cout << "Bubble Sort took " << (end_time-start_time)/1000000. << " seconds." << endl;
    display(b);
    copy(a, b);
    start_time = clock();
    selectionSort(b);
    end_time = clock();
    cout << "Selection Sort took " << (end_time-start_time)/1000000. << " seconds." << endl;
    display(b);
    copy(a, b);
    start_time = clock();
    insertionSort(b);
    end_time = clock();
    cout << "Insertion Sort took " << (end_time-start_time)/1000000. << " seconds." << endl;
    display(b);
    copy(a, b);
    start_time = clock();
    mergesort(b);
    end_time = clock();
    cout << "Mergesort took " << (end_time-start_time)/1000000. << " seconds." << endl;
    display(b);
    copy(a, b);
    start_time = clock();
    quicksort(b);
    end_time = clock();
    cout << "Quicksort took " << (end_time-start_time)/1000000. << " seconds." << endl;
    display(b);
}
