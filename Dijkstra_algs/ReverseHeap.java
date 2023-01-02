
/**
 * ReverseHeap
 * 
 * Author: M. Q. Rieck
 * Date: September 2013
 * 
 */

@SuppressWarnings({"unchecked"})

// Similar to the earlier heap, but lower priorities
// are higher in the heap. Also, floating point priorities
// are used, and can be changed after heap insertion. 

public class ReverseHeap<Data> {

   private static final int MAX_SIZE = 100; 
   // An array of objects to maintain in heap
   private Data data[];
   // An array of associated priorities
   private double priorities[];
   // Size of heap (# nodes in it) 
   private int heapsize;

   private void swapInHeap(int i, int j)
   {
     Data temp = data[i];
     double priority = priorities[i]; 
     data[i] = data[j];
     priorities[i] = priorities[j]; 
     data[j] = temp; 
     priorities[j] = priority;
   }   
   private int parent(int n) { return n/2; }
   private int leftChild(int n) { return 2*n; }
   private int rightChild(int n) { return 2*n+1; }   

   public ReverseHeap() {
      data = (Data[]) new Object[MAX_SIZE];
      priorities = new double[MAX_SIZE];
      heapsize = 0; 
   }
   // Return number of nodes in the heap
   public int getSize() { return heapsize; } 
   // Add a thing with priority to heap, and heapify up 
   public void insertNode(Data d, double priority) {
      int index = ++heapsize;
      data[index] = d;
      priorities[index] = priority;
      while (index > 1 && priorities[index] < priorities[parent(index)])
      {
         swapInHeap(index, parent(index)); 
         index = parent(index);
      }
   }   
   // Remove and return thing on top of heap, and heapify down 
   public Data removeTopOfHeap() {
      int index = 1, indexL, indexR, indexM; 
      if (heapsize == 0) return null;
      // Swap first and last
      swapInHeap(1, heapsize); 
      heapsize--;
      // Heapify down starting at top
      while(index < heapsize) {
         // do child nodes have higher priority? 
         indexM = indexL = indexR = index; 
         if (leftChild(index) <= heapsize) { 
            indexL = leftChild(index);
            if (priorities[indexM] > priorities[indexL]) 
               indexM = indexL; 
         }
         if (rightChild(index) <= heapsize) { 
            indexR = rightChild(index); 
            if (priorities[indexM] > priorities[indexR]) 
               indexM = indexR; 
         }  
         // swap with a child or quit heapifying? 
         if (indexM != index) { 
            swapInHeap(index, indexM); 
            index = indexM;
         } else {
            break;
         }
      }
      return data[heapsize+1];         
   }
   // Change priority of some heap entry
   public void changePriority(Data d, double priority)
   {
      int index, indexL, indexR, indexM;
      double oldPriority;
      for (index=1; index<=heapsize; index++) 
        if (data[index] == d) break;
      if (index == heapsize) return;
      oldPriority = priorities[index];
      priorities[index] = priority; 
      if (oldPriority > priority) {
        while (index > 1 && priorities[index] < priorities[parent(index)]) 
        {
          swapInHeap(index, parent(index)); 
          index = parent(index);
        }
      } else if (oldPriority < priority) { 
        while(index < heapsize) {
          indexM = indexL = indexR = index; 
          if (leftChild(index) <= heapsize) { 
            indexL = leftChild(index);
            if (priorities[indexM] > priorities[indexL]) 
               indexM = indexL; 
          }
          if (rightChild(index) <= heapsize) { 
            indexR = rightChild(index); 
            if (priorities[indexM] > priorities[indexR]) 
               indexM = indexR; 
          }  
          if (indexM != index) { 
            swapInHeap(index, indexM); 
            index = indexM;
          } else {
            break;
          }
        }    
      }
   }
   // Display heap 
   public void display() {
      for (int i=1; i <= heapsize; i++)
         System.out.print("(" + data[i]
           + ":" + priorities[i] + ") ");
      System.out.println();
      System.out.println();
    }   
   // Display each level of heap on separate line 
   public void displayLevels() {
      int count = 0, mark = 1; 
      System.out.println("Levels of the heap:");
      for (int i=1; i <= heapsize; i++) {
         System.out.print("(" + data[i]
           + ":" + priorities[i] + ") "); 
         if (++count == mark) {
             System.out.println();
             count = 0; 
             mark *= 2;
         }
      }
      System.out.println();
      System.out.println();
    }   
}
