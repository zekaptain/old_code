
// Use a greedy algorithm to approximately solve the Knapsack Problem 

import java.util.Scanner;

public class KnapsackGreedy
{
   // Approximately solve Knapsack Problem for capacity cap, n items, values in v and weights in w     
   public static int knap(int cap, int n, int v[], int w[]) 
   {
     int i, j, t, val = 0, valueSum = 0, weightSum = 0;
     double temp; 
     if (n == 0 || cap <= 0) return 0;
     double ratios[] = new double[n]; 
     for (i = 0; i < n; i++) { 
         ratios[i] = (double) v[i] / w[i];
     }
     // Bubble sort ratios into decreasing order 
     for (i = n-1; i > 0; i--) 
       for (j = 0; j < i; j++) 
         if (ratios[j] < ratios[j+1]) {
             temp = ratios[j]; 
             ratios[j] = ratios[j+1];
             ratios[j+1] = temp; 
             t = v[j];
             v[j] = v[j+1]; 
             v[j+1] = t; 
             t = w[j];
             w[j] = w[j+1]; 
             w[j+1] = t; 
         }
     for (i = 0; i < n; i++) {
         if (weightSum + w[i] <= cap) {  
             weightSum += w[i]; 
             valueSum += v[i]; 
         }
     }
     return valueSum; 
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
