
// Use recursion to solve the Knapsack Problem 

import java.util.Scanner;

public class KnapsackRecur
{
   
   // return copy of array minus one element
   public static int[] 
     almostClone(int[] a, int i)
   {
      int j, k, len = a.length;
      int b[] = new int[len-1];
      for (j=k=0; j<len; j++)
        if (j != i) b[k++] = a[j];
      return b;
   }

   // Solve Knapsack Problem for capacity cap, n items, values in v and weights in w 
   public static int knap(int cap, int n, int v[], int w[]) 
   {
     int j, val, max = 0;
     if (n == 0 || cap <= 0) return 0;
     //j is the item that the thief takes. first item thief takes in first subset, second item in second subset, etc.
     for (j = 0; j < n; j++) {
       int[] vp = almostClone(v,j);
       int[] wp = almostClone(w,j);
       if (w[j] <= cap) {
         //this capacity is the current capacity minus the weight of the jth item
        //uses recursion
         val = v[j] + knap(cap-w[j], n-1, vp, wp);
         //keep track of maximum value
         if (val > max) max = val;
       }
     }
     return max; 
   }
   
   public static void main(String[] args) 
   {
       int cap, n, j, value;
       int[] v, w;
       Scanner scan = new Scanner(System.in);
       String again;
       do { 
         System.out.print("Capacity = ");
         cap = scan.nextInt();
         System.out.print("# items = ");
         n = scan.nextInt();
         v = new int[n]; 
         w = new int[n]; 
         for (j=0; j<n; j++) {
           System.out.print("value = "); 
           v[j] = scan.nextInt();
           System.out.print("weight = "); 
           w[j] = scan.nextInt();       
         }
         value = knap(cap, n, v, w);
         System.out.println("Max packing value = " + value);
         System.out.print("Do it again? "); 
         again = scan.next(); 
       } while (again.toUpperCase().charAt(0) == 'Y'); 

   }
}
