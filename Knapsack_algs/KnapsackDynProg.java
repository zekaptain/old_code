
// Use dynamic programming to solve the Knapsack Problem 

import java.util.*;

@SuppressWarnings({"unchecked"})

public class KnapsackDynProg
{
   // A hash table to be used for dynamic programming
   private static Hashtable lookup = new Hashtable();
   // Count number of successful lookups
   private static int count = 0; 
   
   // return copy of array minus one element
   public static int[] almostClone(int[] a, int i)
   {
      int j, k, len = a.length;
      int b[] = new int[len-1];
      for (j=k=0; j<len; j++)
        if (j != i) b[k++] = a[j];
      return b;
   }

   // Represent all Knapsack parameters using a string 
   public static String packInfo(int cap, int n, int v[], int w[]) 
   {
     String s = "" + cap; 
     for (int i = 0; i < n; i++) {
         s += " " + v[i] + " " + w[i]; 
     }
     return s;
   }
   
   // Solve Knapsack Problem for capacity cap, n items, values in v and weights in w  
   public static int knap(int cap, int n, int v[], int w[])
   {
     int j, val, max = 0;
     if (n == 0 || cap <= 0) return 0;
     String key = packInfo(cap, n, v, w);
     Object o; 
     if ((o = lookup.get(key)) != null) {
       count++;
//       System.out.println(key + " : " + ((Integer) o).intValue());
       return ((Integer) o).intValue();     
     } else { 
       for (j = 0; j < n; j++) {
         int[] vp = almostClone(v,j);
         int[] wp = almostClone(w,j);
         if (w[j] <= cap) {
           val = v[j] + knap(cap-w[j], n-1, vp, wp);
           if (val > max) max = val;
         }
       }
       lookup.put(key, new Integer(max)); 
       return max; 
     }
   }
   
   public static void main(String[] args) 
   {
       int cap, n, j, value;
       int[] v, w;
       Scanner scan = new Scanner(System.in);
       String again; 
       do { 
         count = 0; 
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
         System.out.println("# successful lookups = " + count); 
//       System.out.println(lookup);
         System.out.print("Do it again? "); 
         again = scan.next(); 
       } while (again.toUpperCase().charAt(0) == 'Y'); 
   }
}
